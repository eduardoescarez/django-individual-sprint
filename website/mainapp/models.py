from django.db import models

# Create your models here.
class FormularioContactoDB(models.Model):
    nombre  = models.CharField (max_length=30,   null=False, blank=False)
    email   = models.EmailField(max_length=30,   null=False, blank=False)
    asunto  = models.CharField (max_length=30,   null=False, blank=False)
    mensaje = models.CharField (max_length=1000, null=False, blank=False)

class FormularioAsistenciaDB(models.Model):
    nombre  = models.CharField (max_length=30,   null=False, blank=False)
    email   = models.EmailField(max_length=30,   null=False, blank=False)
    area    = models.CharField (max_length=30,   null=False, blank=False)
    asunto  = models.CharField (max_length=30,   null=False, blank=False)
    mensaje = models.CharField (max_length=1000, null=False, blank=False)

class Secciones(models.Model):
    
    class Meta:
        permissions = (
                        ("permiso_clientes", "Permisos necesarios para clientes"),
                        ("permiso_trabajadores", "Permisos necesarios para trabajadores")
                    )
