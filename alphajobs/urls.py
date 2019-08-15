from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Alpha-jobs admin'


urlpatterns = [
    path('admin/', admin.site.urls),
]
