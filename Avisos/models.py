from django.db import models
from django.utils import timezone
from Usuario.models import Usuario
# Create your models here.

class Aviso(models.Model):
    fecha_pub = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL,max_length = 254, blank=True,null=True)
    aviso = models.TextField(max_length = 254, null = True)

        
    def __str__(self):
        return f'{self.autor} - {self.fecha_pub}'