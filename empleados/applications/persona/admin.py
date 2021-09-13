from django.contrib import admin

# Register your models here.
from .models import Persona, Habilidades


class EmpleadoAdmin(admin.ModelAdmin):
    # Especificando que columnas mostrar en las tablas del dashbard
    list_display = (
        'id',
        'first_name',
        'last_name',
        'job',
        'avatar',
        'departamento',
        'full_name' # Columna que no existe en el modelo, se creara temporalmente
    )
    # Especificando sobre qye atributos funcionara el search
    search_fields = (
        'first_name',
        'last_name',
        'job',
        'avatar',
    )
    # Especificando los filtros
    list_filter = (
        'job',
        'departamento',
        'habilities'
    )
    # Especificando que los campos de muchos a muchos al crear un recurso se muestre un diseño con filtro
    filter_horizontal = (
        'habilities',
    )


    # retornara el valor en la columna temporal creada
    def full_name(self, obj):
        # Logica a aplicar por cada registro
        # obj retornara un objeto del modelo especificado
        print(type(obj))
        return f"{obj.first_name} {obj.last_name}"

admin.site.register(Persona, admin_class=EmpleadoAdmin)
admin.site.register(Habilidades)
