from django.urls import path
from . import views

urlpatterns = [
    path('', views.grocery_list, name='grocery_list'),
    path('create/', views.grocery_create, name='grocery_create'),
    path('update/<int:pk>/', views.grocery_update, name='grocery_update'),
    path('delete/<int:pk>/', views.grocery_delete, name='grocery_delete'),
]
