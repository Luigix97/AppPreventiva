from django import forms

from .models import Aulacontenedor, Aulaproductos

class ProductosForm(forms.ModelForm):

    class Meta:
        
        model= Aulaproductos

        fields = [
            'Aula',
            
        ]
        labels = {
            'Aula': 'Seleccionar aula en donde hacen falta los productos',
            
        }
        widgets = {
            'Aula' : forms.Select(attrs={'class': 'form-control'},),
        }

class ContenedorForm(forms.ModelForm):

    class Meta:
        
        model= Aulacontenedor

        fields = [
            'Aula',
            
        ]
        labels = {
            'Aula': 'Seleccionar aula en donde el contentenedor esté lleno',
            
        }
        widgets = {
            'Aula' : forms.Select(attrs={'class': 'form-control'},),
        }