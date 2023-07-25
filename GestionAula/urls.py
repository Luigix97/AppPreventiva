from django.urls import path
from .views import notificarfaltaproductos_view, notificarcontenedor_view, contenedorlleno_list, faltaproductos_list
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('notificarcontenedor/', login_required(notificarcontenedor_view), name='notificarcontenedor'),
    path('notificarproductos/', login_required(notificarfaltaproductos_view), name='notificarproductos'),
    path('lista_contenedores_llenos/', login_required(contenedorlleno_list), name='listacontenedores'),
    path('lista_falta_de_productos/', login_required(faltaproductos_list), name='listaproductos'),
]