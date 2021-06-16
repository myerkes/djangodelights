from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemList.as_view(), name='menu'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    path('ingredients/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('purchases/', views.PurchaseList.as_view(), name='purchases')
]