"""AppPrev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.contrib.auth.views import PasswordChangeView
from .views import InfoPrevencion, Sanciones, DispCubiculos
from GestionAsistencia import views
from Usuario.views import Login, logoutUsuario, ResetContraseña

urlpatterns = [
    path('',RedirectView.as_view(url="infoPrevencion/")),
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('accounts/logout/', login_required(logoutUsuario), name = 'logout'),
    path('accounts/reset_password/', ResetContraseña.as_view, name = 'password_reset'),
    path('usuarios/',include('Usuario.urls')),
    path('quejas/',include('GestionQuejas.urls')),
    path('notificar_aula/', include('GestionAula.urls')),
    path('asistencia_de_profesores/',include('AsistenciaProfesores.urls')),
    path('avisos/', include('Avisos.urls')),
    path('gestion_de_asistencia/', login_required(views.inscribirse_view), name="gestiona"),
    path('registro_asistencia/', login_required(views.inscribirse_list), name="gestiona_registro"),
    path('eliminar_registro/<id>/', login_required(views.inscribirse_delete), name="eliminar"),
    path('ubicaciones/', login_required(views.ubicaciones_list), name='ubicaciones'),
    path('infoPrevencion/', InfoPrevencion, name="InfoPrevencion"),
    path('sanciones/', Sanciones, name="sanciones"),
    path('DispCubiculos/', login_required(DispCubiculos), name='DispCubiculos'),
    
]