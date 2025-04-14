from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin-panel/', views.admin_panel),
    path('usuario/', views.usuario_portal),
    path('api/medicos/', views.listar_medicos),
    path('api/cadastrar-medico/', views.cadastrar_medico),
    path('api/cadastrar-usuario/', views.cadastrar_usuario),
    path('api/agendar-consulta/', views.agendar_consulta),
    path('api/excluir-consulta/', views.excluir_consulta),
]
