from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('api/habitaciones/', include('apps.habitaciones.urls')),
    path('api/reservas/', include('apps.reservas.urls')),
    path('api/finanzas/', include('apps.finanzas.urls')),
     path('api/hoteles/', include('apps.hoteles.urls')),
]
