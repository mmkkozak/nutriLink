from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from . import views

app_name = 'nutriLink'

urlpatterns = [
    path("", views.index, name="index"),

    # path("contact/", views.contact, name="contact"),
    path('new/', views.new_recipe, name="new_recipe"),
    path('<int:pk>/', views.recipe, name="recipe"),
    path('profile/', views.profile, name="user")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
