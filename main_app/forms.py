from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    city = forms.CharField(label = "City")
    startdate = forms.DateField
    class Meta:
        model = User
        fields = ("username", "city", "email",)
        help_texts= ""

