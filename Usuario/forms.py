from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'contraseña'
        
        

class FormularioUsuario(forms.ModelForm):
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de confirmación', widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese de nuevo su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ['rol','username','email','nombres','apellidos','expediente']
        widgets = {
            'email' : forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                }
            ),
            'nombres' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su/s nombre/s',
                }
            ),
            'apellidos' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'username' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            ),
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user