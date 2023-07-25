from django import forms

from .models import Alumnos,Clases,Ubicaciones

class gestionForm(forms.ModelForm):

    class Meta:
        model = Alumnos

        fields = [
            'materiaAsistir',
        ]
        labels = {
            'materiaAsistir': 'Materia A Inscribirse',
        }
        widgets = {
            'materiaAsistir' : forms.Select(attrs={'class': 'form-control'},),
        }

