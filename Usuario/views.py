from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Usuario
from .forms import FormularioLogin, FormularioUsuario

# Create your views here.


class Login(FormView):
    template_name = 'registration/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('InfoPrevencion')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')

class ResetContraseña(PasswordChangeView):
    template_name = 'registration/password_reset_form.html'
    email_template= 'registration/password_reset_email.html'

class ListadoUsuarios(ListView):
    model = Usuario
    template_name = 'Usuario/lista_de_usuarios.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active = True)

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'Usuario/crear_usuario.html'
    success_url = reverse_lazy('lista_de_usuarios')

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                rol = form.cleaned_data.get('rol'),
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos'),
                expediente = form.cleaned_data.get('expediente'),
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('lista_de_usuarios')
        else:
            return render(request,self.template_name,{'form':form})

class EditarUsuario(UpdateView):
    model = Usuario
    template_name = 'Usuario/crear_usuario.html'
    form_class = FormularioUsuario
    success_url = reverse_lazy('lista_de_usuarios')

class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('lista_de_usuarios')