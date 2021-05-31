from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname = forms.CharField(label="Enter last name", max_length = 100)
    class Meta:
        model = User
        fields = ['username', 'firstname','lastname','email', 'password1', 'password2']