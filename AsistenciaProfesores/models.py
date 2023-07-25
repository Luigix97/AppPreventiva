from django.db import models
from Usuario.models import Usuario
from GestionAsistencia.models import Clases

# Create your models here.

class AsistenciaProfesor(models.Model):
    Tipos_de_asistencia= [
        {'Sí sistiré','Asistiré'},
        {'Llegaré 15 minutos después','Llegaré 15 minutos tarde'},
        {'No iré','No asistiré'},
    ]
    profesor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank= True, null= True)
    materia = models.ForeignKey(Clases, on_delete=models.SET_NULL, blank= True, null= True)
    tipo = models.CharField(choices = Tipos_de_asistencia, max_length=50, blank= True, null= True)
    mensaje = models.TextField(max_length=254, blank=True, null=True)
    dia = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.profesor} - {self.tipo} - {self.dia}'