from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import DepartamentoForm
from applications.persona.models import Persona
from .models import Departamento


# FormView
# Permite definir clases que no especifican propia mente un modelo
# Util cuando se deben modificar al tiempo varios modelos
class DepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    # Asignando la clase del form
    form_class = DepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print("Interceptando el form")

        # Creando el departamento
        name = form.cleaned_data['name']
        short_name = form.cleaned_data['short_name']
        departamento = Departamento(
            name=name,
            short_name=short_name,
        )
        departamento.save()

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        # Creando el empleado
        Persona.objects.create(
            first_name=first_name,
            last_name=last_name,
            job='1',
            departamento=departamento
        )

        return super(DepartamentoView, self).form_valid(form)
