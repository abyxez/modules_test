from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Module
from .serializers import ModuleCreateSerializer, ModuleListSerializer


class CreateListUpdateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class ModuleViewSet(CreateListUpdateDestroyViewSet):
    queryset = Module.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ("name",)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action in [
            "list",
        ]:
            return ModuleListSerializer
        return ModuleCreateSerializer
