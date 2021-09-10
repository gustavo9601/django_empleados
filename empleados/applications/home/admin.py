from django.contrib import admin
from .models import Home

# Añadiendo el modelo al administrador propio de django
admin.site.register(Home)
