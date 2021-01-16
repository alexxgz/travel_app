from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
class RegisterForm(UserCreationForm):
    city = forms.ChoiceField(choices=[(1,'Seattle'),(2,'San Francisco'),(3,'New York'),(4,'London'),(5,'Hong Kong')])   
    class Meta:
        model = User
        fields = ("username", "city", "email",)
        help_texts= ""