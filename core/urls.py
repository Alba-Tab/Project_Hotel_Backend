from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register(r"habitaciones", HabitacionViewSet)

urlpatterns = [path("", include(router.urls))]