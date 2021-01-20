from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=250, default='')
    image = models.URLField((""), max_length=1000, default='')
    country = models.CharField(max_length=250, default='')
    # def __str__(self):
    #     return self.name
       
class Profile(AbstractUser):
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    # def __str__(self):
    #     return self.name
class Meta:
    ordering = ['-date']

