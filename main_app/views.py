from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import City, Post 
from .forms import RegisterForm, EditUserForm, Post_Form, City_Form, Edit_Post_Form


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


def cities_show(request, city_id):
  posts = Post.objects.all()
  cities = City.objects.filter(id=city_id)
  context = {
    'cities': cities, 
    'posts': posts
    }
  return render(request, 'cities/show.html', context)


def posts_show(request, post_id):
  current_user = request.user
  post = Post.objects.get(id=post_id)
  cities = City.objects.all()
  if request.user.is_authenticated:
    context = {
      'user': current_user,
      'cities': cities, 
      'post': post,
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

def make_post(request):
  error_message=''
  if request.method == "POST":
    form = Post_Form(request.POST)
    if form.is_valid():
      author = request.user
      article = Post
      print(author.id)
      print(article.user)
      article = form.save(commit=False)
      article.user = author
      article.save()
      return redirect('profile')
    else:
      print(form.errors)
      error_message = 'Invalid post input'
  current_user = request.user
  form = Post_Form(initial={'city' : current_user.city})
  context= {'form' : form, 'error_message': error_message, 'user': current_user}
  return render(request, 'posts/new.html', context)
  
def edit_post(request, post_id):
  current_post = Post.objects.get(id=post_id)
  if request.method == 'POST':
    form = Post_Form(request.POST, instance=current_post)
    if form.is_valid():
      post = Post.objects.get(id=post_id)
      if request.POST['title']:
        post.title = request.POST['title']
      if request.POST['body']:
        post.body = request.POST['body']
      post.city = request.POST['city']
      post.save()
      return redirect('profile')
    else:
      print(form.errors)
      error_message = 'Invalid input'
  form = Edit_Post_Form(initial={'title' : current_post.title, 'body' : current_post.body})
  context = {'form' : form, 'post' : current_post}
  return render(request, 'posts/edit.html', context)
