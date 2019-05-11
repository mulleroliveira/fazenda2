from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('animais/', views.animals),
    path('animais/excluir/<int:id_animal>/', views.delete_animal),
    path('animais/cadastrar/', views.register_animal),
    path('animais/editar/<int:id_animal>/', views.edit_animal),]