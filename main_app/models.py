from django.db import models
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class City:
    def __init__(self, name, state):
        self.name = name 
        self.state = state

cities = [
    City('San Francisco', 'California')
]

# users = [
#     User('Bob', 'Smith', "Lorem Epsom", "New York City")
# ]

# class User:
#     def __init__(self, first_name, last_name, posts, current_city):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.posts = posts
#         self.current_city = current_city