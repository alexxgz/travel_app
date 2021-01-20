from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import City, Post 
from .forms import RegisterForm, EditUserForm, Post_Form, City_Form


# Create your views here.

def home(request):
  return render(request, 'home.html')


def profile(request):
  user = request.user
  posts = Post.objects.all()
  if request.user.is_authenticated:
    context = { 
      'user': user,
      'posts': posts
      }
    return render(request, 'user/profile.html', context)
  else:
    return redirect('acounts/signup')

def about(request):
  return HttpResponse('<h1>About</h1>')


def cities_show(request):
  posts = Post.objects.all()
  cities = City.objects.all()
  context = {
    'cities': cities, 
    'posts': posts
    }
  return render(request, 'cities/show.html', context)


def posts_show(request):
  current_user = request.user
  posts = Post.objects.all()
  cities = City.objects.all()
  if request.user.is_authenticated:
    context = {
      'user': current_user,
      'cities': cities, 
      'posts': posts,
      }
    return render(request, 'posts/show.html', context)
  else:
    return redirect('acounts/signup')


def cities_index(request):
  posts = Post.objects.all()
  cities = City.objects.all()
  context = {
    'cities': cities,
    'posts': posts,
    }
  return render(request, 'cities/index.html', context)


def signup(request):
  error_message=''
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      profile = form.save()
      login(request, profile)
      return redirect('profile')
    else:
      print(form.errors)
      error_message = 'Invalid sign up'
  form = RegisterForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def edit_profile(request):
  if request.method == 'POST':
    form = EditUserForm(request.POST)
    if form.is_valid():
      user = request.user
      if request.POST['username']:
        user.username = request.POST['username']
      user.city = request.POST['city']
      user.save()
      return redirect('profile')
    else:
      print(form.errors)
      error_message = 'Invalid input'
  current_user = request.user
  form = EditUserForm(initial={'city' : current_user.city})
  context = {'form': form, 'user': current_user}
  return render(request, 'user/edit.html', context)


  
