from django.contrib import admin

# Register your models here.
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase, Order

admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirements)
admin.site.register(Purchase)
admin.site.register(Order)