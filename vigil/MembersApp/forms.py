from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserInfoForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)