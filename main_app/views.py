from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import City, Post 



# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return HttpResponse('<h1>About</h1>')

def posts_show(request):
  context = {
    'cities': cities, 
    'posts': posts
    }
  return render(request, 'posts/show.html', context)

def cities_index(request):
  context = {
    'cities': cities, 
    'posts': posts
    }
  return render(request, 'cities/index.html', context)


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

def signup(request):
  error_message=''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

