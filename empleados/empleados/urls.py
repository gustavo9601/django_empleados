from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from applications.departamento.urls import url_departameto
from applications.home.urls import urls_home
from applications.persona.urls import urls_personas

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluimos las urls de app departamento
    path('', include(url_departameto)),
    # Home
    path('', include(urls_home)),
    # Persona
    path('', include(urls_personas))

]

# Adding the debug query in dashboard admin
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path(r'^__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
