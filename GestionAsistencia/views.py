from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.db.models.functions import Now

#nuevo
from .models import Clases
from .models import Alumnos 
from .models import Ubicaciones
from .forms import gestionForm
from django.contrib import messages

from django.db.models import QuerySet, OuterRef

# Create your views here.

#def Gestiona(request):

 #   return render(request, "pages/gestiona.html")

def inscribirse_view(request):

    clase = Clases.objects.all().order_by('horario')    
    #form = gestionForm()
    #now = datetime.now()

    #alumnos = Alumnos.objects.filter(materiaAsistir__horario__lte=Now()).values('materiaAsistir')
    clases = Clases.objects.filter(horario__lte=Now()).filter(cupoDisponible__gt=0)
    #alumnos = Alumnos.objects.all()

    form = gestionForm(request.POST or None)
    form.fields["materiaAsistir"].queryset = clases

    if request.method == 'POST':
        #form = gestionForm(request.POST)

        if form.is_valid():
            ObjetoQueSeCreo = form.save(commit = False)
            
            ObjetoQueSeCreo.expediente = request.user.expediente
            ObjetoQueSeCreo.nombre = request.user

            alumno = Alumnos.objects.filter(expediente = request.user.expediente)
            registros = alumno.filter(materiaAsistir = ObjetoQueSeCreo.materiaAsistir)

            if registros:
                messages.warning(request, 'La inscripción ya existe')
            else:
                ObjetoQueSeCreo.save()
                messages.success(request, 'Inscripcion realizada con exito')
            

        redirect('pages/gestiona')
        form = gestionForm()

    return render(request, 'pages/gestiona.html', {'form':form, 'clases': clase})
 

def inscribirse_list(request):
    #alumno = Alumnos.objects.filter(expediente = 1).order_by('materiaAsistir__horario')#.values('materiaAsistir')

    #clase = Clases.objects.filter(id__in = alumno)
    alumno = Alumnos.objects.filter(expediente = request.user.expediente).order_by('materiaAsistir__horario')#.values('materiaAsistir')


    contexto = {'alumnos' : alumno} #, 'clases':clase}

    return render(request, 'pages/gestiona_registro.html', contexto)

def inscribirse_delete(request,id) :
    alumno = Alumnos.objects.get(id = id)

    if request.method == 'POST':
        alumno.delete()
        return redirect('gestiona_registro')
    
    return render(request, 'pages/Eliminar_registro.html', {'alumno': alumno})

def ubicaciones_list(request):
    ubicaciones = Ubicaciones.objects.all()

    return render(request, 'pages/ubicaciones.html', {'Ubicaciones': ubicaciones})