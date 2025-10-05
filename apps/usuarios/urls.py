from django.urls import path, include

urlpatterns = [
    path("api/usuarios/", include("apps.usuarios.urls")),
]
