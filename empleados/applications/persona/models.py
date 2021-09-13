from django.db import models

from applications.departamento.models import Departamento


# Create your models here.
class Persona(models.Model):
    """ Modelo para tabla empleado  """""
    first_name = models.CharField(verbose_name='Nombres', max_length=50)
    last_name = models.CharField(verbose_name='Apellidos', max_length=50)

    # Creando similar a un Enum y solo permita valores permitidos
    # En el admin se mostrara como una select html
    JOB_CHOICES = [
        ('1', 'CONTADOR'),
        ('2', 'ADMINISTRADOR'),
        ('3', 'ECONOMIESTA'),
        ('4', 'OTRO'),
    ]

    job = models.CharField(verbose_name='Trabajos', max_length=50, choices=JOB_CHOICES)

    # Creando la relacion y campo con el modelo departamento
    # relacion de uno a muchos
    departamento = models.ForeignKey(to=Departamento, on_delete=models.CASCADE)

    # image = models.ImageField()

    def __str__(self):
        return f"{self.id} | {self.first_name} | {self.last_name} | {self.job} | {self.departamento}"

