from django import forms

class SignUpForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100)
    user_email = forms.EmailField(label="E-mail", max_length=100)
    user_password = forms.CharField(label="Password", max_length=100)
    password_confirm = forms.CharField(label="Confirm Password", max_length=100)

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Username", max_length=100)
    user_password = forms.CharField(label="Password", max_length=100)