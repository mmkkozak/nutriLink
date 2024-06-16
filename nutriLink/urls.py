from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("<int:recipe_id>/", views.recipe, name="recipe"),

    path("<int:user_id>/user/", views.user, name="user"),

    path("<int:user_id>/recipe_form/", views.recipe_form, name="recipe_form"),

    path("user_form/", views.user_form, name="user_form")
]