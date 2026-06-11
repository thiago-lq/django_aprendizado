from django.urls import path
from . import views

urlpatterns = [
    path('listar-usuarios', views.listar_usuarios, name='listar_usuarios'),
    path('cadastrar-usuario', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('editar-usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('deletar-usuario/<int:pk>/', views.deletar_usuario, name='deletar_usuario')
]