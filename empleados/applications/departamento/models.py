from django.db import models


# Create your models here.
class Departamento(models.Model):
    # verbose_name= // valor a mostrar en el administrador django
    name = models.CharField(verbose_name='Nombre', max_length=200)
    short_name = models.CharField(verbose_name='Nombre Corto', max_length=20, unique=True)
    active = models.BooleanField(verbose_name='Activo', default=False)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.short_name} | {self.active}"
