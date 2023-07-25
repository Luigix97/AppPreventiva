from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import AsistenciaForm
from .models import AsistenciaProfesor
from django.utils import timezone
from django.contrib import messages


# Create your views here.
class ListarAsistencia(ListView):
    model = AsistenciaProfesor
    template_name = 'pages/lista_de_asistencia_profe.html'

    def get_queryset(self):
        return self.model.objects.filter(dia__contains = timezone.localdate())

class SeleccionarAsistencia(CreateView):
    model = AsistenciaProfesor
    form_class = AsistenciaForm
    template_name = 'pages/seleccionar_asistencia_profe.html'

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = AsistenciaForm(request.POST)
            if form.is_valid():
                asistencia = form.save(commit = False)
                asistencia.profesor = request.user
                asistencia.save()
                messages.success(request, 'Asistencia notificada con exito')
        else:
            form = AsistenciaForm()
        return render(request, 'pages/seleccionar_asistencia_profe.html', {'form':form})
    