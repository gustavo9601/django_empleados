from django.urls import path

from . import views

urls_personas = [
    path(route='listar-empleados', view=views.ListAllPersonas.as_view()),
    path(route='listar-empleados-por-area/<str:departamento>', view=views.ListAllPersonasByArea.as_view()),
]
