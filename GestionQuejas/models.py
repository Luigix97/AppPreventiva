from django.db import models

# Create your models here.

class NotificacionQuejas(models.Model):

    Queja = models.CharField( max_length=254, blank = True, null = True)

    def __str__(self):
        return '%s' (self.Queja)
