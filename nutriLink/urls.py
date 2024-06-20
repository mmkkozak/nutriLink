from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings

from .forms import LoginForm
from django.contrib import admin

from . import views

app_name = 'nutriLink'

urlpatterns = [
    path("", views.index, name="index"),

    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='nutriLink/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page' : settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path('new/', views.new_recipe, name="new_recipe"),
    path('<int:pk>/', views.recipe, name="recipe"),

    path('profile/', views.profile, name="user"),

    path('recipe_text/<int:pk>/', views.recipe_text, name="recipe_text")

]
