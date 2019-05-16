from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('animals/', views.animals),
    path('animals/delete/<int:id_animal>/', views.delete_animal),
    path('animals/register/', views.register_animal),
    path('animals/edit/<int:id_animal>/', views.edit_animal),
    path('creators/', views.creators),
    path('creators/delete/<int:id_creator>/', views.delete_creator),
    path('creators/register/', views.register_creator),
    path('creators/edit/<int:id_creator>/', views.edit_creator),
    path('farms/', views.farms),
    path('farms/delete/<int:id_farm>/', views.delete_farm),
    path('farms/register/', views.register_farm),
    path('farms/edit/<int:id_farm>/', views.edit_farm),
    ]