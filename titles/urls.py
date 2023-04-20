from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ModuleViewSet

app_name = "titles"

router = DefaultRouter()
router.register("titles", ModuleViewSet, basename="titles")

urlpatterns = [
    path("v1/", include(router.urls)),
]
