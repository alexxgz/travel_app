from django.forms import ModelForm
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

class RegisterForm(UserCreationForm):
    city = forms.ChoiceField(choices=[('Seattle','Seattle'),('San Fancisco','San Francisco'),('New York','New York'),('London','London'),('Hong Kong','Hong Kong')])   
    class Meta:
        model = Profile
        fields = ("username", "city", "email",)
        help_texts= ""