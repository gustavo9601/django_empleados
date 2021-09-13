from django.db import models

from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    hability = models.CharField(verbose_name='Habilidad', max_length=50)

    class Meta:
        # Nombre a mostrar en el dashboard
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f"{self.id} | {self.hability}"


class Persona(models.Model):
    """ Modelo para tabla empleado  """""
    first_name = models.CharField(verbose_name='Nombres', max_length=50)
    last_name = models.CharField(verbose_name='Apellidos', max_length=50)
    nickname = models.CharField(verbose_name='Apodo generado automaticamente', max_length=100, blank=True, null=True)

    # Creando similar a un Enum y solo permita valores permitidos
    # En el admin se mostrara como una select html
    JOB_CHOICES = [
        ('1', 'CONTADOR'),
        ('2', 'ADMINISTRADOR'),
        ('3', 'ECONOMIESTA'),
        ('4', 'OTRO'),
    ]

    job = models.CharField(verbose_name='Trabajos', max_length=50, choices=JOB_CHOICES)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)

    # Creando la relacion y campo con el modelo departamento
    # relacion de uno a muchos
    departamento = models.ForeignKey(to=Departamento, on_delete=models.CASCADE)

    # relacion muchos a muchos
    habilities = models.ManyToManyField(Habilidades)

    curriculum_vitae = RichTextField(verbose_name='Hoja de vida', null=True, blank=True)

    class Meta:
        # Nombre a mostrar en el dashboard
        verbose_name = 'Personal'
        verbose_name_plural = 'Mi Personal'
        # Ordenamiento
        ordering = ['-first_name']
        # Permite validar convinaciones de cambos y verificar que esa conbinacion no se repita
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f"{self.id} | {self.first_name} | {self.last_name} | {self.job} | {self.departamento}"
