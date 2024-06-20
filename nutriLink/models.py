from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=150, unique=True)
    user = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    contents = models.TextField()
    picture = models.ImageField(upload_to='uploads/')
    pub_date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    kcal = models.IntegerField()
    amount = models.IntegerField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, related_name='created_reviews', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='recipe_reviews', on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField()
    other_measure = models.CharField(max_length=100, blank=True, null=True)

class Diet(models.Model):
    diet_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.diet_name

class Exclusion(models.Model):
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    max_amount = models.IntegerField()

    def __str__(self):
        return self.ingredient.name