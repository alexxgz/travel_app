from django.forms import ModelForm
from django import forms
from .models import Profile, Post, City
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from datetime import datetime

class RegisterForm(UserCreationForm):
    city = forms.ChoiceField(choices=[('Seattle','Seattle'),('San Fancisco','San Francisco'),('New York','New York'),('London','London'),('Hong Kong','Hong Kong')]) 
    class Meta:
        model = Profile
        fields = ("username", "city", "email",)
        help_texts= ""
class EditUserForm(UserChangeForm):
    city = forms.ChoiceField(choices=[('Seattle','Seattle'),('San Fancisco','San Francisco'),('New York','New York'),('London','London'),('Hong Kong','Hong Kong')])
    username = forms.CharField(max_length=254, required=False)
    class Meta:
        model = Profile
        exclude = ("password1", "password2")
        fields = ("username", "city",)
        help_texts= ""

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


class City_Form(ModelForm):
    class Meta:
        model = City
        fields = ['city', 'image', 'country']
