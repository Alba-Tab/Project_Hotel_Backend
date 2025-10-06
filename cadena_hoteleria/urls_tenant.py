from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('core.urls')),
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('api/habitaciones/', include('apps.habitaciones.urls')),
    path('api/reservas/', include('apps.reservas.urls')),
    path('api/finanzas/', include('apps.finanzas.urls')),
]