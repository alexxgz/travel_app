from django.forms import ModelForm, ModelChoiceField
from django import forms
from .models import Profile, Post, City
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from datetime import datetime

class CityModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.city
class RegisterForm(UserCreationForm):
    city = CityModelChoiceField(queryset=City.objects.all())
    class Meta:
        model = Profile
        fields = ("username", "city", "email",)
        help_texts= ""
class EditUserForm(UserChangeForm):
    city = CityModelChoiceField(queryset=City.objects.all())
    username = forms.CharField(max_length=254, required=False)
    password=None
    class Meta:
        model = Profile
        exclude = ("password1", "password2")
        fields = ("username", "city",)
        help_texts= ""

class Post_Form(ModelForm):
    city = CityModelChoiceField(queryset=City.objects.all())
    title = forms.CharField(max_length=254, required=True)
    body = forms.CharField(max_length=10000, required=True, widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'body', 'city']

class Edit_Post_Form(ModelForm):
    city = CityModelChoiceField(queryset=City.objects.all())
    title = forms.CharField(max_length=254, required=True)
    body = forms.CharField(max_length=10000, required=True, widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'body', 'city']

class City_Form(ModelForm):
    class Meta:
        model = City
        fields = ['city', 'image', 'country']


        
