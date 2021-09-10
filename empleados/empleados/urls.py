from django.contrib import admin
from django.urls import path, include
from applications.departamento.urls import url_departameto
from applications.home.urls import urls_home

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluimos las urls de app departamento
    path('', include(url_departameto)),
    # Home
    path('', include(urls_home)),

]
