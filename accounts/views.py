from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from knox.models import AuthToken


from .serializers import LoginSerializer, RegisterSerializer, UserSerializer


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data ,
            'token': AuthToken.objects.create(user)[1]
        })



class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)   
        user = serializer.validated_data
        return Response({
            'user' :UserSerializer(user, context=self.get_serializer_context()).data,
            'token':AuthToken.objects.create(user)[1]
        })
