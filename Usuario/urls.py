from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListadoUsuarios, RegistrarUsuario, EditarUsuario, EliminarUsuario


urlpatterns = [
    path('lista_de_usuarios/', login_required(ListadoUsuarios.as_view()), name = 'lista_de_usuarios'),
    path('registrar_usuario/', login_required(RegistrarUsuario.as_view()), name = 'registrar_usuario'),
    path('editar_usuario/<int:pk>/', login_required(EditarUsuario.as_view()), name = 'editar_usuario'),
    path('eliminar_usuario/<int:pk>/', login_required(EliminarUsuario.as_view()), name = 'eliminar_usuario'),
]