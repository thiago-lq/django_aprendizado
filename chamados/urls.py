from django.urls import path
from . import views

urlpatterns=[
    path('listar-chamados', views.listar_chamados, name='listar_chamados'),
    path('ver-chamado/<int:pk:/', views.ver_chamado, name='ver_chamado'),
    path('cadastrar-chamado', views.cadastrar_chamado, name='cadastrar_chamado'),
    path('editar-chamado/<int:pk>/', views.editar_chamado, name='editar_chamado'),
    path('deletar-chamado/<int:pk>/', views.deletar_chamado, name='deletar_chamado')
]