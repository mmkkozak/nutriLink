from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

"""
class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
"""

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=150, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    picture = models.ImageField(upload_to='uploads/')
    pub_date = models.DateTimeField(auto_now_add=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    kcal = models.IntegerField()
    amount = models.IntegerField()
    unit = models.CharField(max_length=20)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    pub_date = models.DateTimeField()

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField()
    other_measure = models.CharField(max_length=100, blank=True, null=True)

class Diet(models.Model):
    diet_name = models.CharField(max_length=100, unique=True)
    # exclusion

class Exclusion(models.Model):
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    max_amount = models.IntegerField()

