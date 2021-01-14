from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import City

# Create your views here.

def home(request):
  return render(request, 'home.html')


def about(request):
  return HttpResponse('<h1>About</h1>')