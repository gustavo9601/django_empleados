from django.urls import path

from . import views

urls_personas = [
    path(route='listar-empleados', view=views.ListAllPersonas.as_view()),
    path(route='detalle-empleado/<int:pk>', view=views.DetailPersonaView.as_view()),
    path(route='listar-habilidades-empleados/<int:id>', view=views.ListHabilidadesPersona.as_view()),
    path(route='buscar-empleados', view=views.ListAllPersonasByKWord.as_view()),
    path(route='listar-empleados-por-area/<str:departamento>', view=views.ListAllPersonasByArea.as_view()),
]
