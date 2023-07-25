from django import forms
from .models import Aviso

class AvisoForm(forms.ModelForm):

    class Meta:
        model = Aviso

        fields = ['aviso']
        labels = {'aviso': 'Mensaje / Aviso'}
        widgets = {
            'aviso': forms.Textarea(attrs={'class': 'form-control'})
        }
        
