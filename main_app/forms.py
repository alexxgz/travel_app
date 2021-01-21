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
    city = forms.ChoiceField(choices=[(1,'Seattle'),(2,'San Francisco'),(3,'New York'),(4,'London'),(5,'Hong Kong')])
    title = forms.CharField(max_length=254, required=True)
    body = forms.CharField(max_length=10000, required=True, widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'body', 'city']

class Edit_Post_Form(ModelForm):
    city = forms.ChoiceField(choices=[(1,'Seattle'),(2,'San Francisco'),(3,'New York'),(4,'London'),(5,'Hong Kong')])
    title = forms.CharField(max_length=254, required=True)
    body = forms.CharField(max_length=10000, required=True, widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'body', 'city']

class City_Form(ModelForm):
    class Meta:
        model = City
        fields = ['city', 'image', 'country']
