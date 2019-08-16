from django.urls import path
from .views import RegisterAPIView , LoginAPIView
from knox.views import LogoutView


app_name = 'accounts'

urlpatterns = [
    #TODO: Password reset urln
    #TODO: add this url to home urls file 
    #FIXME: Add comma after every created path
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
