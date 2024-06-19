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

    path('<int:pk>/', views.recipe, name="recipe"),

    path('signup/', views.signup, name="signup"),

    path('login/', auth_views.LoginView.as_view(template_name='nutriLink/login.html', authentication_form=LoginForm), name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
