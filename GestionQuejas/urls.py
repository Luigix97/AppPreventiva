from django.urls import path
from .views import notificarquejas_views, quejas_list
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('notificar_queja/', login_required(notificarquejas_views), name='notificarqueja'),
    path('lista_quejas/', login_required(quejas_list), name='listarquejas'),
] 