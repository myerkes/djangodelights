from typing import List
from inventory.models import Ingredient, MenuItem, Purchase
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

class MenuItemList(ListView):
    model = MenuItem
    context_object_name = 'menuitem_list'
    template_name = 'inventory/menuitem_list.html'

class IngredientList(ListView):
    model = Ingredient
    context_object_name = 'ingredient_list'
    template_name = 'inventory/ingredient_list.html'

class PurchaseList(ListView):
    model = Purchase
    context_object_name = 'purchase_list'
    template_name = 'inventory/purchase_list.html'