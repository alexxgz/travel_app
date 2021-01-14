from django.db import models

# Create your models here.
class City:
    def __init__(self, name, state):
        self.name = name 
        self.state = state
        

cities = [
    City('San Francisco', 'California'),
    City('New York City', 'New York')
]


class Post:
    def __init__(self, title, city, body):
        self.title = title
        self.city = city
        self.body = body

posts = [
    Post('Great Tacos', 'San Francisco', 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'),
    Post('Great Pizza', 'New York', 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')

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

