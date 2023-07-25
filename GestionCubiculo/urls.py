from django.urls import path
from .views import Cubiculos_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('DispCubiculos/', login_required(Cubiculos_view()), name='DispCubiculos'),
   
]