from rest_framework import serializers

from .models import Module


class ModuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = (
            "name",
            "description",
        )


class ModuleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
        read_only_fields = ("name", "description")
