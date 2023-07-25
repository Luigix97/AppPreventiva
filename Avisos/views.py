from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.utils import timezone
from .forms import AvisoForm
from .models import Aviso

# Create your views here.

class ListarAvisos(ListView):
    model = Aviso
    template_name = 'pages/avisos.html'
    context_object_name = 'avisos'
    queryset = Aviso.objects.all()

class CrearAviso(CreateView):
    model = Aviso
    form_class = AvisoForm
    template_name = 'pages/Hacer_aviso.html'
    succes_url = reverse_lazy('avisos')

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form = AvisoForm(request.POST)
            if form.is_valid():
                aviso = form.save(commit=False)
                aviso.autor = request.user
                aviso.save()
                return redirect('avisos')
        else:
            form = AvisoForm()
        
        return render(request, 'pages/Hacer_aviso.html', {'form':form})
    