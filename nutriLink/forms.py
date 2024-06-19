from django import forms
from datetime import datetime
from .models import Recipe

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class SignUpForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100)
    user_email = forms.EmailField(label="E-mail", max_length=100)
    user_password = forms.CharField(label="Password", max_length=100)
    password_confirm = forms.CharField(label="Confirm Password", max_length=100)

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100)
    user_password = forms.CharField(label="Password", max_length=100)

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
            'picture': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
    # recipe_name = forms.CharField(label="Recipe Name", max_length=150)
    # contents = forms.CharField(label="Contents")
    # picture = forms.CharField(label="Picture")
    # pub_date = forms.DateTimeField(label="DateTime")

