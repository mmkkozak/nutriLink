from django import forms
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Recipe, Review

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Twoja nazwa użytkownika",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Twój e-mail",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Twoje hasło",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Powtórz hasło",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Nazwa użytkownika",
        "class": 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Hasło',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'contents', 'picture')

        widgets = {
            'recipe_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'contents': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            # 'picture': forms.FileInput(attrs={
            #     'class': INPUT_CLASSES
            # })
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('stars', 'comment')
        widgets = {
                'stars': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
                'comment': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            })
        }
        labels = {
            'stars': "Gwiazdki",
            'comment': "Komentarz"
        }