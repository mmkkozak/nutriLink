from django.urls import path

from . import views

app_name = 'nutriLink'

urlpatterns = [
    path("", views.index, name="index"),

    path("<int:recipe_id>/", views.recipe, name="recipe"),

    path("<int:user_id>/user/", views.user, name="user"),

    path("<int:user_id>/recipe_form/", views.new_recipe, name="recipe_form"),

    path("user_form/", views.user_form, name="user_form"),

    path("sign_up/", views.get_new_user, name="sign_up"),

    path('insert_user/', views.insertUser, name='insert_user'),

    path('sign_in/', views.loginUser, name='sign_in'),

    path('redirect/', views.verify_user, name='verify_user'),

    path('<int:user_id>/insert_recipe/', views.insert_recipe, name='insert_recipe')

]