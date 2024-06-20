from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from django.contrib import admin

from . import views

app_name = 'nutriLink'

urlpatterns = [
    path("", views.index, name="index"),

    # path("contact/", views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
path('login/', auth_views.LoginView.as_view(template_name='nutriLink/login.html', authentication_form=LoginForm), name='login'),
    path('new/', views.new_recipe, name="new_recipe"),
    path('<int:pk>/', views.recipe, name="recipe"),
<<<<<<< Updated upstream
    path('profile/', views.profile, name="user")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======

    path('profile/', views.profile, name="user"),

    path('recipe_text/<int:pk>/', views.recipe_text, name="recipe_text")

]
>>>>>>> Stashed changes
