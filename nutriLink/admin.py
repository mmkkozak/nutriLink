from django.contrib import admin

# Register your models here.
from .models import Ingredient, Exclusion, Diet

admin.site.register(Ingredient)
admin.site.register(Exclusion)
admin.site.register(Diet)