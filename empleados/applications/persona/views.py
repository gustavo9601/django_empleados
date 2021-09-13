from django.shortcuts import render
from django.views.generic import (ListView)
from .models import Persona


# Create your views here.
class ListAllPersonas(ListView):
    model = Persona
    template_name = 'personas/list_all.html'
    # define el nombre de variable a enviar al html
    # si no se especifica el content, se retornara la data en la variable object_list al template
    context_object_name = 'personas'


class ListAllPersonasByArea(ListView):
    """ Lista de personas por area """
    model = Persona
    template_name = 'personas/list_all.html'
    # define el nombre de variable a enviar al html
    # si no se especifica el content, se retornara la data en la variable object_list al template
    context_object_name = 'personas'

    """
    # departamento__name // Departamento.name
    queryset = Persona.objects.filter(
        departamento__name = 'tecnologia'
    )"""

    # Funcion que tiene la logica de reemplazo para consultar sobre la bd
    def get_queryset(self):

        # accediendo a los valores enviados por la url y definidos en esta
        departamento = self.kwargs['departamento']

        data = Persona.objects.filter(
            departamento__name=departamento
        )
        return data
