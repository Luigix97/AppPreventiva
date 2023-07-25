from django.http import HttpResponse
from django.shortcuts import render


def Contacto(request):

    return render(request, "pages/contacto.html")

def InfoPrevencion(request):

    return render(request, "pages/InfoPrevencion.html")

def Sanciones(request):

    return render(request, "pages/sanciones.html")

def DispCubiculos(request):

    return render(request, "pages/DispCubiculos.html")



