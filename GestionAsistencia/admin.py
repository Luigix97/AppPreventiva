from django.contrib import admin
from .models import Alumnos
from .models import Ubicaciones
from .models import Clases

# Register your models here.

admin.site.register(Ubicaciones)
#admin.site.register(Alumnos)
admin.site.register(Clases)