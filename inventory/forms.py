from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, Order
from django import forms

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
