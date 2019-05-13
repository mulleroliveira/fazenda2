from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('animais/', views.animals),
    path('animais/excluir/<int:id_animal>/', views.delete_animal),
    path('animais/cadastrar/', views.register_animal),
    path('animais/editar/<int:id_animal>/', views.edit_animal),
    path('criadores/', views.creators),
    path('criadores/excluir/<int:id_creator>/', views.delete_creator),
    path('criadores/cadastrar/', views.register_creator),
    path('criadores/editar/<int:id_creator>/', views.edit_creator),
    path('fazendas/', views.farms),
    path('fazendas/excluir/<int:id_farm>/', views.delete_farm),
    path('fazendas/cadastrar/', views.register_farm),
    path('fazendas/editar/<int:id_farm>/', views.edit_farm),
    ]