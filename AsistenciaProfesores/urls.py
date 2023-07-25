from django.urls import path
from .views import ListarAsistencia, SeleccionarAsistencia
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('lista_de_asistencia/', login_required(ListarAsistencia.as_view()), name='lista_asistencias_profes'),
    path('seleccionar_asistencia/', login_required(SeleccionarAsistencia.as_view()), name='seleccionar_asistencia'),
]