from django.urls import path
from main import views
from . import views
from django.views.generic import TemplateView

#Nomes da rotas seguem o padrão: só nome = deslogado, cli_ = cliente, fun_ = funcionario
urlpatterns = [
    #cliente
    path('', views.home, name='url_home'),
    path('deslatendimentos', views.desl_atendimentos, name='desl_atendimentos'),
    path('inicio/', views.ClienteList.as_view(), name='cli_home'),
    path('updateCliente/<int:pk>/', views.ClienteUpdate.as_view(), name='url_updatecliente'),
    
    
    #login
    path('cadastroCliente/', views.ClienteCreate.as_view(), name='url_cadastroClientes'),
    path('loginCliente/', views.ClienteList.as_view(), name='login'),
    #path('login/', views.login.as_view(), name='url_login'),

    #funcionario
    path('iniciofun/', views.FunList.as_view(), name='url_homeFun'),
    path('updateFuncionario/<int:pk>/', views.FunUpdate.as_view(), name='url_updateFuncionario'),
    path('listCliFunc/', views.FunClienteList.as_view(), name='url_clientesFun'),

    path('animal/', views.AnimalList.as_view(), name='url_animais'),
    path('cadastroAnimal/', views.AnimalCreate.as_view(), name='url_cadastroanimal'),
    path('updateAnimal/<int:pk>/', views.AnimalUpdate.as_view(), name='url_updateAnimal'),
    path('deleteAnimalFun/<int:pk>/', views.AnimalDelete.as_view(), name='url_deleteAnimal'),
    path('atendimentos', views.atendimentoListFun.as_view(), name='url_atendimentosFun'),

    path('animalCli/', views.AnimalListCli.as_view(), name='url_animaisCli'),
    path('cadastroAnimalCli/', views.AnimalCreateCli.as_view(), name='url_cadastroanimalcli'),
    path('updateAnimalCli/<int:pk>/', views.AnimalUpdateCli.as_view(), name='url_updateAnimalCli'),
    path('deleteAnimalCli/<int:pk>/', views.AnimalDeleteCli.as_view(), name='url_deleteAnimalCLi'),


    #atendimentos

    path('atendimentos', views.atendimentoListFun.as_view(), name='url_atendimentos'),
    path('cadastroAtendimentosFun/', views.AtendimentoCreateFun.as_view(), name='url_cadastroAtendimentos'),
    path('updateAtendimentoFun/<int:pk>/', views.AtendimentoUpdateFun.as_view(), name='url_updateatendimento'),
    path('deleteAtendimentoFun/<int:pk>/', views.AtendimentoDeleteFun.as_view(), name='url_deleteAtendimento'),

    path('atendimentosCli', views.atendimentoListCli.as_view(), name='url_atendimentosCli'),
    path('cadastroAtendimentoscli/', views.AtendimentoCreateFunCli.as_view(), name='url_cadastroAtendimentoscli'),
    path('updateAtendimentocli/<int:pk>/', views.AtendimentoUpdateCli.as_view(), name='url_updateAtendimentoCli'),
    path('deleteAtendimentocli/<int:pk>/', views.AtendimentoDeleteCli.as_view(), name='url_deleteAtendimentoCli'),

    path('contato/', views.contato.as_view(), name='url_contato'),
    
]