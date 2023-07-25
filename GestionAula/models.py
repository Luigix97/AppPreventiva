from django.db import models

from GestionAsistencia.models import Ubicaciones


class Aulaproductos(models.Model):
    Aula = models.ForeignKey(Ubicaciones,on_delete=models.CASCADE, null=True)
    Hora = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return '%s' % (self.Aula)

class Aulacontenedor(models.Model):   
    Aula = models.ForeignKey(Ubicaciones,on_delete=models.CASCADE, null=True)
    Hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return '%s' % (self.Aula)
