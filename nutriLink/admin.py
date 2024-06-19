from django.contrib import admin

# Register your models here.
from .models import Ingredient, Exclusion, Diet, User

admin.site.register(Ingredient)
admin.site.register(Exclusion)
admin.site.register(Diet)
admin.site.register(User)