from django import forms

from .models import Cubiculos

class CubiculoForms(forms.ModelForm):

    class Meta:
        
        model= Cubiculos

        fields = [
            'ocupado',
            'desocupado',
        ]
        labels = {
            'ocupado': 'Ocupado',
            'desocupado': 'Desocupado',
        }
        widgets = {
            'ocupado' : forms.CheckboxInput(attrs={'class': 'form-control'},),
            'desocupado' : forms.CheckboxInput(attrs={'class': 'form-control'},)
        }