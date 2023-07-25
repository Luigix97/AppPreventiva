from django.db import models

# Create your models here.

class Cubiculos(models.Model):
    ocupado = models.BooleanField()
    desocupado = models.BooleanField()
    mensaje = models.TextField()
  
    
    def __str__(self):
         return '%s %s' % (self.ocupado,self.desocupado,self.mensaje)