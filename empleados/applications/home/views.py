from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView


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

