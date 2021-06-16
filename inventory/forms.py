from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, Order
from django import forms

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
