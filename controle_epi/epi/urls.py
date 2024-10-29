from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    #URLs para o modulo de epi
    path('', views.index, name='index'),
    path('listar/', views.listar_epi, name='listar_epi'),
    path('cadastrar/', views.cadastrar_epi, name='cadastrar_epi'),
    path('atualizar/', views.atualizar_epi, name='atualizar_epi_tela'),
    path('atualizar/<int:id>/', views.atualizar_epi, name='atualizar_epi'),
    path('excluir/<int:id>/', views.excluir_epi, name='excluir_epi'),
    #URLs para o modulo de colaboradores
    path('listar_colaborador/', views.listar_colaborador, name='listar_colaborador'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('atualizar_colaborador/', views.atualizar_colaborador, name='atualizar_colaborador_tela'),
    path('atualizar_colaborador/<int:id>/', views.atualizar_colaborador, name='atualizar_colaborador'),
    path('excluir_colaborador/<int:id>/', views.excluir_colaborador, name='excluir_colaborador'),
    #URL para o modulo de registrar ação
    path('registrar_acao/', views.registrar_acao, name='registrar_acao'),
    path('listar_acao/', views.listar_acao, name='listar_acao'),
    path('atualizar_acao/', views.atualizar_acao, name='atualizar_acao_tela'),
    path('atualizar_acao/<int:id>/', views.atualizar_acao, name='atualizar_acao'),
<<<<<<< HEAD
    path('excluir_acao/<int:id>/', views.excluir_acao, name='excluir_acao'),
=======
>>>>>>> 57783c8b0168f365d2a802178f4c0f61ecd41bf5
    #Loguin e Logout
    path('login/', auth_views.LoginView.as_view(template_name='epi/globals/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
