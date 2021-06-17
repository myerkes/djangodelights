from typing import List
from django.db.models import Sum
from django.views.generic.base import TemplateView
from inventory.models import Ingredient, MenuItem, Purchase
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from .forms import *

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html')

### Registration Views ###
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

@login_required
def logout_request(request):
  logout(request)
  return redirect("index")

### Menu Item Views ###
class MenuItemList(ListView):
    model = MenuItem
    context_object_name = 'menuitem_list'
    template_name = 'inventory/menuitem_list.html'

class MenuItemCreate(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'inventory/menuitem_create_form.html'
    form_class = MenuItemCreateForm

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'inventory/menuitem_update_form.html'
    form_class = MenuItemUpdateForm

class MenuItemDelete(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'inventory/menuitem_delete_form.html'
    success_url = '/menu/'

### Ingredient Views ###
class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    context_object_name = 'ingredient_list'
    template_name = 'inventory/ingredient_list.html'

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create_form.html'
    form_class = IngredientCreateForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update_form.html'
    form_class = IngredientUpdateForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete_form.html'
    success_url = '/ingredients/'

### Recipe Requirement Views ###
class RecipeRequirementList(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    context_object_name = 'reciperequirement_list'
    template_name = 'inventory/reciperequirement_list.html'

class RecipeRequirementCreate(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_create_form.html'
    form_class = RecipeRequirementCreateForm

class RecipeRequirementUpdate(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_update_form.html'
    form_class = RecipeRequirementUpdateForm

class RecipeRequirementDelete(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = 'inventory/reciperequirement_delete_form.html'
    success_url = '/reciperequirement/'

### Purchase Views ###
class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    context_object_name = 'purchase_list'
    template_name = 'inventory/purchase_list.html'

class PurchaseCreate(CreateView):
    model = Purchase
    template_name = 'inventory/purchase_create_form.html'
    form_class = PurchaseCreateForm

### Order Views ###
class OrderList(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'inventory/order_list.html'

class OrderCreate(CreateView):
    model = Order
    template_name = 'inventory/order_create_form.html'
    form_class = OrderCreateForm

### Summary Views ###
class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/sales_report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(
            revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                total_cost += recipe_requirement.ingredient.price_per_unit * \
                    recipe_requirement.quantity

        context["revenue"] = revenue
        context["total_cost"] = total_cost
        context["profit"] = revenue - total_cost

        return context
