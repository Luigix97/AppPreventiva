from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Rol(models.Model):
    id = models.AutoField(primary_key = True)
    rol = models.CharField('Rol', max_length = 50, unique = True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rols'

    def __str__(self):
        return self.rol
    
    def save(self,*args,**kwargs):
        permisos_defecto = ['add','change','delete','view']
        if not self.id:
            nuevo_grupo,creado = Group.objects.get_or_create(name = f'{self.rol}')
            for permiso_temp in permisos_defecto:
                permiso,created = Permission.objects.update_or_create(
                    name = f'Can {permiso_temp} {self.rol}',
                    content_type = ContentType.objects.get_for_model(Rol),
                    codename = f'{permiso_temp}_{self.rol}',
                )
                if creado:
                    nuevo_grupo.permissions.add(permiso.id)
            super().save(*args,**kwargs)
        else:
            rol_antiguo = Rol.objects.filter(id = self.id).values('rol').first()
            if rol_antiguo['rol'] == self.rol:
                super().save(*args,**kwargs)
            else:
                Group.objects.filter(name = rol_antiguo['rol']).update(name = f'{self.id}')
                for permiso_temp in permisos_defecto:
                    Permission.objects.filter(codename = f"{permiso_temp}_{rol_antiguo['rol']}").update(
                        codename = f'{permiso_temp}_{self.rol}',
                        name = f'Can {permiso_temp} {self.rol}'
                    )
                super().save(*args,**kwargs)

            

class UsuarioManager(BaseUserManager):
    def _create_user(self,username,email,nombres,apellidos,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            email = email,
            nombres = nombres,
            apellidos = apellidos,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,username,email,nombres,apellidos, password = None,**extra_fields):
        return self._create_user(username, email, nombres, apellidos, password, False, False,**extra_fields)
    
    def create_superuser(self,username,email,nombres,apellidos,password = None,**extra_fields):
        return self._create_user(username, email, nombres, apellidos, password, True, True,**extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    rol = models.ForeignKey(Rol, on_delete = models.CASCADE, blank = True, null = True)
    username = models.CharField('Nombre de usuario', unique = True, max_length = 40)
    nombres = models.CharField('Nombres', max_length = 30, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length = 30, blank = True, null = True)
    expediente = models.IntegerField('Expediente', unique = True, blank = True, null = True)
    email = models.EmailField('Correo electrónico', max_length = 254, unique = True)
    imagen = models.ImageField('Imagen de perfil', upload_to = None, max_length = None, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UsuarioManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def save(self,*args,**kwargs):
        if not self.id:
            super().save(*args,**kwargs)
            if self.rol is not None:
                grupo = Group.objects.filter(name = self.rol.rol).first()
                if grupo:
                    self.groups.add(grupo)
                super().save(*args,**kwargs)
            else:
                if self.rol is not None:
                    grupo_antiguo = Usuario.objects.filter(id = self.id).values('rol__rol').first()
                    if grupo_antiguo['rol__rol'] == self.rol.rol:
                        super().save(*args,**kwargs)
                    else:
                        grupo_anterior = Group.objects.filter(name = grupo_antiguo['rol__rol']).first()
                        if grupo_antiguo:
                            self.groups.remove(grupo_anterior)
                            nuevo_grupo = Group.objects.filter(name = self.rol.rol).first()
                            if nuevo_grupo:
                                self.groups.add(nuevo_grupo)
                            super().save(*args,**kwargs)
