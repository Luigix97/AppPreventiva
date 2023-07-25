from django import forms

from .models import NotificacionQuejas

class gestiondeForm(forms.ModelForm):

    class Meta:
        
        model= NotificacionQuejas

        fields = [
            'Queja'
            
        ]

        labels = {
            'Queja': 'Redacte su queja',
            
        }
        widgets = {
            'Queja' : forms.Textarea(attrs={'class': 'form-control', 
            'placeholder' : 'Redacte su queja en este espacio'},),
            
        }