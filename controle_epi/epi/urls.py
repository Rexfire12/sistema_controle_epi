from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar_epi, name='listar_epi'),
    path('cadastrar/', views.cadastrar_epi, name='cadastrar_epi'),
    path('atualizar/', views.atualizar_epi, name='atualizar_epi_tela'), #FIXME Ajustar essa linha
    path('atualizar/<int:id>/', views.atualizar_epi, name='atualizar_epi'),
    path('excluir/<int:id>/', views.excluir_epi, name='excluir_epi'),
    path('listar_usuario/', views.listar_usuarios, name='listar_usuario'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    #path('atualizar_usuario/<int:id>/', views.atualizar_usuario, name='atualizar_usuario'),
   # path('excluir_usuario/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
