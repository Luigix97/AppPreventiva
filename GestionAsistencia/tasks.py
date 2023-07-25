from __future__ import absolute_import
from GestionAsistencia.models import Alumnos
from django.utils import timezone

from celery import shared_task


@shared_task
def add(x, y):
    return x + y

@shared_task
def eliminarRegistros():
    alumnos = Alumnos.objects.all()

    for alumno in alumnos:
        if alumno.materiaAsistir__horario < timezone.now():
            alumno.delete()

    return "Se eliminaron los registros a las {}".format(timezone.now())