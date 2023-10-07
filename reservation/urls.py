from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
]
