from django.contrib import admin
from related_admin import RelatedFieldAdmin
from .models import Job , Location




class JobAdmin(RelatedFieldAdmin):
    list_display = ('address__city','address__country', 'pay_per_day')
    list_filter =  ('address__city' , 'address__country', 'pay_per_day')
admin.site.register(Job, JobAdmin)


