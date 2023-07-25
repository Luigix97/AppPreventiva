from django import forms
from .models import AsistenciaProfesor

class AsistenciaForm(forms.ModelForm):

    class Meta:
        model = AsistenciaProfesor

        fields = [
            'materia',
            'tipo',
            'mensaje',
        ]
        labels = {
            'materia': 'Clase a notificar asistencia',
            'tipo': 'Tipo de asistencia',
            'mensaje':'Mensaje complementario',
        }
        widgets = {
            'materia': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
