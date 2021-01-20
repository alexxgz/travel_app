from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=250, default='')
    image = models.URLField((""), max_length=1000, default='')
    country = models.CharField(max_length=250, default='')
    def __str__(self):
        return self.name

        
class Profile(AbstractUser):
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

# class Post:
#     def __init__(self, title, city, body):
#         self.title = title
#         self.city = city
#         self.body = body

# posts = [
#     Post('Great Tacos', 'San Francisco', 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'),
#     Post('Great Pizza', 'New York', 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

# ]

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    def __str__(self):
        return self.name

