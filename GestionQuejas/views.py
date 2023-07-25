from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.db.models.functions import Now

from .forms import gestiondeForm
from GestionQuejas.models import NotificacionQuejas
from django.contrib import messages
# Create your views here.

def notificarquejas_views(request):

    form = gestiondeForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            QuejaCreada = form.save()

            QuejaCreada.save()
                
            messages.success(request, 'La queja ha sido enviada con éxito')

        redirect('pages/notificarqueja')
    
    form = gestiondeForm()

    return render (request, 'pages/notificarqueja.html', {'form':form})

def quejas_list(request):

    queja = NotificacionQuejas.objects.all()

    contexto = {'quejas':queja}

    return render(request, 'pages/listar_quejas.html', contexto)
