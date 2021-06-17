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
    path('reciperequirement/', views.RecipeRequirementList.as_view(), name='reciperequirements'),
    path('reciperequirement/create', views.RecipeRequirementCreate.as_view(), name='reciperequirementcreate'),
    path('reciperequirement/update/<pk>', views.RecipeRequirementUpdate.as_view(), name='reciperequirementupdate'),
    path('reciperequirement/delete/<pk>', views.RecipeRequirementDelete.as_view(), name='reciperequirementdelete'),
    path('purchases/', views.PurchaseList.as_view(), name='purchases'),
    path('purchases/create', views.PurchaseCreate.as_view(), name='purchasecreate'),
    path('order/', views.OrderList.as_view(), name='orders'),
    path('order/create', views.OrderCreate.as_view(), name='ordercreate')
]