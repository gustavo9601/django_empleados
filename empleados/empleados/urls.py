from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# // extiende las urls que se generan automaticamente espeficando la url de setting y la carpeta condetendora
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Adding the debug query in dashboard admin
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path(r'^__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
