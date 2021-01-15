from django.forms import ModelForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    city = forms.CityField(label = "City")
    startdate = models.DateTimeField(auto_now_add = True)
    class Meta:
        model = User
        fields = ("username", "city", "email",)
        help_texts= ""