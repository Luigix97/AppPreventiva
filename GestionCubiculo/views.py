from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db.models.functions import Now

from .forms import CubiculoForms
from GestionAula.models import Cubiculos
from django.contrib import messages

from django.db.models import QuerySet, OuterRef

def Cubiculos_view(request):
    
    form = ()

    form = CubiculoForms(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            CubiculoOcupado = form.save()

            CubiculoOcupado.save()
                
            messages.success(request, 'El cubículo esta ocupado')

        redirect('pages/DispCubiculos')
        form = CubiculoForms()

    return render (request, 'pages/DispCubiculos.html', {'form':form})

