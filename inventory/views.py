from inventory.models import MenuItem
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