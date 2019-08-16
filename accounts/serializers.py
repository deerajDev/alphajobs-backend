from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' , 'email' , 'user_work_ratings', 'user_pay_ratings')
    


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password':{'style' : {'input_type': 'password', 'placeholder': 'Password'}, 'write_only':True}}
    
    #TODO: Learn when this will be called
    def create(self, validated_data):
        instance= User.objects.create_user(validated_data['email'], validated_data['password'])
        return instance
        
    
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=20,required=True , style={'input_type':'password','placeholder':'password'})
    #setting for password field
    extra_kwargs = {'password':{'style' : {'input_type': 'password', 'placeholder': 'Password'}, 'write_only':True}}

    def validate(self,data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect email or password')





'''
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

    return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")


'''