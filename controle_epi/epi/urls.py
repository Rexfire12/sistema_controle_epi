from django.urls import path
from epi import views

urlpatterns = [
    path('', views.index),
    path('', views.listar_epi, name='listar_epi'),
    path('cadastrar/', views.criar_epi, name='criar_epi'),
    path('deletar/<int:id>/', views.deletar_epi, name='deletar_epi'),
    path('atualizar/<int:id>/', views.atualizar_epi, name='atualizar_epi'),
]
