from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.db.models.functions import Now

from .forms import ContenedorForm, ProductosForm
from GestionAula.models import Aulaproductos, Aulacontenedor
from django.contrib import messages

# Create your views here.

def notificarfaltaproductos_view(request):
    
    form = ProductosForm()

    form = ProductosForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            AulafaltapCreada = form.save()

            AulafaltapCreada.save()
                
            messages.success(request, 'La notificación ha sido enviada con éxito')

        redirect('pages/notificarproductos')
        form = ProductosForm()

    return render (request, 'pages/notificarproductos.html', {'form':form})

def notificarcontenedor_view(request):

    form = ContenedorForm

    form = ContenedorForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            ContenedorLlenoCreado = form.save()

            ContenedorLlenoCreado.save()
                
            messages.success(request, 'Se ha notificado el contenedor en su capacidad máxima con éxito')

        redirect('pages/notificarContenedor')
        form = ContenedorForm()

    return render (request, 'pages/notificarContenedor.html', {'form':form})

def faltaproductos_list(request):

    falta = Aulaproductos.objects.all()

    contexto = {'faltas':falta}

    return render(request, 'pages/listar_productos.html', contexto)

def contenedorlleno_list(request):

    lleno = Aulacontenedor.objects.all()

    contexto = {'llenos':lleno}

    return render(request, 'pages/listar_contenedor.html', contexto)