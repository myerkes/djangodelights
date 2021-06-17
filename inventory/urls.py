from django.urls import path, include
from django.contrib.auth import logout
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_request, name='logout'),
    path('menu/', views.MenuItemList.as_view(), name='menu'),
    path('menu/create', views.MenuItemCreate.as_view(), name="menuitemcreate"),
    path('menu/update/<pk>', views.MenuItemUpdate.as_view(), name="menuitemupdate"),
    path('menu/delete/<pk>', views.MenuItemDelete.as_view(), name="menuitemdelete"),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients'),
    path('ingredients/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredients/update/<pk>', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('ingredients/delete/<pk>', views.IngredientDelete.as_view(), name='ingredientdelete'),
    path('purchases/', views.PurchaseList.as_view(), name='purchases')
]