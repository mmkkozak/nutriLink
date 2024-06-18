from django import forms
from datetime import datetime
from django.db import models

class SignUpForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100)
    user_email = forms.EmailField(label="E-mail", max_length=100)
    user_password = forms.CharField(label="Password", max_length=100)
    password_confirm = forms.CharField(label="Confirm Password", max_length=100)

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100)
    user_password = forms.CharField(label="Password", max_length=100)

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(label="Recipe Name", max_length=150)
    contents = forms.CharField(label="Contents")
    picture = forms.CharField(label="Picture")
    pub_date = forms.DateTimeField(label="DateTime")

