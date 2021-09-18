from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from .models import Home
from .forms import HomeForm

# Create your views here.
class HomeView(TemplateView):
    # Define el archivo html a retornar ./templates/home.html
    template_name = 'home/home.html'


# ListView // Sirve para listar y renderizar multiples cosas
class HomeListView(ListView):
    # Especificando el nombre de la variable que se enviara a la vista
    context_object_name = 'list_gretting'
    # Especifica manualmente los valores de la lista a enviar a la vista
    queryset = [
        'Hello', 'world'
    ]
    template_name = 'home/list.html'


# Usando un modelo de datos
class HomeListTestView(ListView):
    model = Home
    context_object_name = 'data'
    template_name = 'home/test_list.html'


# Clase que permite crear un recurso
class HomeCreateView(CreateView):
    model = Home
    template_name = 'home/add_home.html'
    # Especifica campos que se podran recibir para crear
    # fields = ['titulo', 'subtitulo', 'cantidad']

    # Usando una clase para especificar la clase separando la responsabilidad
    form_class = HomeForm
    success_url = '/'

