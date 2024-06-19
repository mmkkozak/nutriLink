from django import forms
from datetime import datetime
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(label="Recipe Name", max_length=150)
    contents = forms.CharField(label="Contents")
    picture = forms.CharField(label="Picture")
    pub_date = forms.DateTimeField(label="DateTime")

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Your e-mail",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm your password",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your username",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Your password",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))