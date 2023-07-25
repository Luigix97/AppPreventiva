from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum


# Create your models here.

class Ubicaciones(models.Model):
    nombre = models.CharField(max_length=50)
    capacidadActual = models.IntegerField()
    capacidadMaxima = models.IntegerField()
    estadoActual = models.BooleanField()
    aforo = models.FloatField(default = 0)

    def __str__(self):
        return self.nombre 

class Clases(models.Model):
    nombre = models.CharField(max_length=50)
    horario = models.TimeField()
    profesor = models.CharField(max_length=50)
    cupoDisponible = models.IntegerField()
    ubicacion = models.ForeignKey(Ubicaciones,on_delete=models.SET_NULL, null=True)

    def __str__(self):
         return '%s %s %s' % (self.nombre, self.horario, self.ubicacion)

class Alumnos(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    expediente = models.IntegerField(blank=True,null=True)
    materiaAsistir = models.ForeignKey(Clases,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}, {self.expediente}'

@receiver(post_save, sender=Alumnos)
def actualizar_cupo(sender, instance, **kwargs):

    clase_id = instance.materiaAsistir.id

    clase = Clases.objects.get(pk = clase_id)

    ubicacion_id = clase.ubicacion_id

    ubicacion = Ubicaciones.objects.get(pk = ubicacion_id)

    if ubicacion:
        ubicacion.capacidadActual = Alumnos.objects.filter(materiaAsistir = clase_id).count()
        ubicacion.aforo = (ubicacion.capacidadActual*100)/ubicacion.capacidadMaxima
        ubicacion.save()

    if clase:
        clase.cupoDisponible =  ubicacion.capacidadMaxima - ubicacion.capacidadActual 
        clase.save()