from django.forms import ModelForm
from django.contrib.auth.models import User

class UserCreationForm(ModelForm):
    class Meta:
        help_texts= ""