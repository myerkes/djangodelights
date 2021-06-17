from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, Order
from django import forms

### Ingredient Forms ###
class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

### Menu Item Forms ###
class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuItemUpdateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

### Recipe Requirement Forms ###
class RecipeRequirementCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'

class RecipeRequirementUpdateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'

### Purchase Forms ###
class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

### Order Forms ###
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


    items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.IntegerField
    )