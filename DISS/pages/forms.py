from django import forms
from django.forms import ModelForm
from .models import *

class LoginForm(forms.Form):
    email = forms.CharField(label = "Email", max_length = 255)
    password = forms.CharField(label = "Password", widget = forms.PasswordInput())

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password','first_name','last_name']

