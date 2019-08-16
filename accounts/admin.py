from django.contrib import admin
from django.contrib.auth.models import  Group
from .models import  User

admin.site.unregister(Group)



class UserAdmin(admin.ModelAdmin):
    list_display = ('email','user_pay_ratings', 'user_work_ratings')

admin.site.register(User, UserAdmin)
