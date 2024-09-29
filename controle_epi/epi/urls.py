from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_epi, name='cadastrar_epi'),
    path('atualizar/<int:id>/', views.atualizar_epi, name='atualizar_epi'),
    path('listar/', views.listar_epi, name='listar_epi'),
]
