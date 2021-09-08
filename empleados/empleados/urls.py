from django.contrib import admin
from django.urls import path, include
from applications.departamento.urls import url_departameto

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluimos las urls de app departamento
    path('', include(url_departameto))

]
