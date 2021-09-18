from django.urls import path

from . import views

# personas:<<name_path>>
urls_personas = ([

                     path(route='', view=views.InitView.as_view(), name='inicio'),

                     path(route='listar-empleados', view=views.ListAllPersonas.as_view(), name='personas-all'),
                     path(route='success', view=views.SuccessViews.as_view(), name='success'),
                     path(route='crear-empleado', view=views.CreatePersonaView.as_view()),
                     path(route='actualizar-empleado/<int:pk>', view=views.UpdateEmpleadoView.as_view(), name='update'),
                     path(route='eliminar-empleado/<int:pk>', view=views.DeleteEmpleadoView.as_view(), name='delete'),
                     path(route='detalle-empleado/<int:pk>', view=views.DetailPersonaView.as_view(), name='detalle-empleado'),
                     path(route='listar-habilidades-empleados/<int:id>', view=views.ListHabilidadesPersona.as_view()),
                     path(route='buscar-empleados', view=views.ListAllPersonasByKWord.as_view(), name='buscar-persona-by-kword'),
                     path(route='listar-empleados-por-area/<str:departamento>',
                          view=views.ListAllPersonasByArea.as_view()),
                 ], "personas")
