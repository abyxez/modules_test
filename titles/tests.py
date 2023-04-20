import unittest

from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Module, User
from .serializers import ModuleCreateSerializer, ModuleListSerializer
from .views import ModuleViewSet


@unittest.skipIf(
    len([method for method in dir(Module)
         if method.startswith("__") is False]) < 1,
    "No class methods to test yet!",
)
class TestModuleModel(TestCase):
    """Тестируем модель."""

    def setUp(self) -> None:
        self.module = Module.objects.create(
            name="Math",
            description="Lessons of math",
        )

    def test_module_fields(self):
        self.assertEqual(self.module.name, "Math")
        self.assertEqual(self.module.description, "Lessons of math")


class TestSerializer(TestCase):
    """Тестируем сериализатор."""

    def test_serializer(self):
        data = {
            "name": "Physics",
            "description": "Some physical tests",
        }
        serializer = ModuleCreateSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, data)


@override_settings(ROOT_URLCONF="modules.urls")
class TestViewset(TestCase):
    """Тестируем вьюсет."""

    def setUp(self) -> None:
        self.client = APIClient()
        self.viewset = ModuleViewSet.as_view({"get": "list"})
        self.url = reverse("API:titles-list")
        self.model = Module.objects.create(
            name="Russian", description="Russian language"
        )
        self.user = User.objects.create(username="Tester")

    def test_viewset_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = ModuleListSerializer(self.model)
        obj = response.json()["results"][0]
        self.assertEqual(obj, serializer.data)

    def test_viewset_post(self):
        self.client.force_login(self.user)
        data = {
            "name": "Physics",
            "description": "Some physical tests",
        }
        self.client.post(
            self.url,
            data=data,
        )
        self.assertTrue(
            Module.objects.filter(
                name=data["name"], description=data["description"]
            ).exists()
        )


if __name__ == "__main__":
    unittest.main()
