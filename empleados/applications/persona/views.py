from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView)
from .models import Persona
from django.urls import reverse_lazy


# Create your views here.
class ListAllPersonas(ListView):
    model = Persona
    template_name = 'personas/list_all.html'
    # define el nombre de variable a enviar al html
    # si no se especifica el content, se retornara la data en la variable object_list al template
    context_object_name = 'personas'

    # Paginacion
    # Recibe el valor a mostrar por peticion, y por get capturara automaticamente el page
    paginate_by = 2


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


class ListAllPersonasByKWord(ListView):
    """Lista de empleados por palabta clave"""
    template_name = 'personas/list_all.html'
    context_object_name = 'personas'

    def get_queryset(self):
        # Capturando por get el parametro ?kword
        key_word = self.request.GET.get('kword')
        print("key_word >>", key_word)
        data = Persona.objects.filter(
            first_name=key_word
        )
        return data


class ListHabilidadesPersona(ListView):
    template_name = 'personas/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        # accediendo a los valores enviados por la url y definidos en esta
        id = self.kwargs['id']
        # Recuperando un unico registro de persona
        persona = Persona.objects.get(id=id)
        # Accediendo a la relacion directa del modelo Persona con habiltiies
        habilidades = persona.habilities.all()
        return habilidades


class DetailPersonaView(DetailView):
    model = Persona
    context_object_name = 'persona'
    template_name = 'personas/detail_persona.html'

    # Enviando mas variables al template, se debe sobreescribir el metodo
    def get_context_data(self, **kwargs):
        context = super(DetailPersonaView, self).get_context_data(**kwargs)
        print("context detail >>", context)
        # Añadiendo al contexto al html
        context['titulo'] = 'Empleado del mes'

        return context


class CreatePersonaView(CreateView):
    model = Persona
    template_name = 'personas/add.html'
    # Indicarle que atributos del modelo se permitiran pintar y actualizar
    # fields = ('__all__') # permite generar todos los campos
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilities']

    # Define a donde se debe redirigir cuando se complete el proceso
    # usando reverse_lazy se le pasa el nombre de la url
    success_url = reverse_lazy(viewname='personas:success')

    # sobrescribiendo el metodo despues de guardarlo, para adicionar el valor en la nueva columna
    def form_valid(self, form):
        print(type(form))
        # Ya se guardo el registro y retorna una instancia del modelo
        empleado = form.save()
        # Modificando la propiedad
        empleado.nickname = empleado.first_name[0:2] + '-' + empleado.last_name[0:2]
        # Guardando nuevamente el modelo
        empleado.save()
        return super(CreatePersonaView, self).form_valid(form)


class SuccessViews(TemplateView):
    template_name = 'personas/success.html'


class UpdateEmpleadoView(UpdateView):
    template_name = 'personas/update.html'
    model = Persona
    # fields = ('__all__')  # permite generar todos los campos
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilities']
    success_url = reverse_lazy(viewname='personas:success')

    # Sobrescribe el metodo antes de validar los datos
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("****************************")
        print("request.POST >> ", request.POST)
        return super(UpdateEmpleadoView, self).post(request, *args, **kwargs)


class DeleteEmpleadoView(DeleteView):
    model = Persona
    # Template que es usado para confirmar la eliminacion
    template_name = 'personas/delete.html'
    success_url = reverse_lazy(viewname='personas:success')


class InitView(TemplateView):
    """View load init page"""
    template_name = 'personas/inicio.html'