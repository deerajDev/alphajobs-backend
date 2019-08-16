from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Alpha-jobs admin'


urlpatterns = [
    #FIXME: Add comma after every path
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
]
