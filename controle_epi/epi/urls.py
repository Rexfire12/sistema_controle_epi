from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_epi, name='listar_epi'),
    path('cadastrar/', views.cadastrar_epi, name='cadastrar_epi'),
    path('atualizar/', views.atualizar_epi, name='atualizar_epi_tela'), #FIXME Ajustar essa linha
    path('atualizar/<int:id>/', views.atualizar_epi, name='atualizar_epi'),
    path('excluir/<int:id>/', views.excluir_epi, name='excluir_epi'),
    #URLs para o modulo de colaboradores
    path('listar_colaborador/', views.listar_colaborador, name='listar_colaborador'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('atualizar_colaborador/', views.atualizar_colaborador, name='atualizar_colaborador_tela'),
    path('atualizar_colaborador/<int:id>/', views.atualizar_colaborador, name='atualizar_colaborador'),
    path('excluir_colaborador/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),
]
