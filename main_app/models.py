from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser, User
import django.utils.timezone

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
    body = models.CharField(max_length=5000)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    timestamp = models.DateTimeField(default=django.utils.timezone.now)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1, related_name="posts")
class Meta:
    ordering = ['-date']

