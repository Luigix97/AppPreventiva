from django.urls import path
from .views import ListarAvisos, CrearAviso
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('lista_avisos/', login_required(ListarAvisos.as_view()), name='avisos'),
    path('hacer_aviso/', login_required(CrearAviso.as_view()), name='crear_aviso'),
]