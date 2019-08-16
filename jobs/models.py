from django.db import models 
from django.contrib.auth import  get_user_model




#user model or tabel
user = get_user_model()


class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    street = models.CharField(max_length=40,blank=False)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    



class Job(models.Model):
    creator = models.ForeignKey(user, related_name='proposals', on_delete=models.CASCADE)      
    description = models.TextField()
    pay_per_day = models.IntegerField(blank=False, null=False)
    num_days  =  models.IntegerField()
    address = models.ForeignKey(Location,  related_name='jobs' ,  on_delete=models.CASCADE)



class CityJobs(models.Model):
  nearest_job = models.ForeignKey('Job', related_name='city_jobs', on_delete=models.CASCADE)