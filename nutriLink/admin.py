from django.contrib import admin

# Register your models here.
from .models import Ingredient, Exclusion, Diet, Recipe, Review

admin.site.register(Ingredient)
admin.site.register(Exclusion)
admin.site.register(Diet)
admin.site.register(Recipe)
admin.site.register(Review)