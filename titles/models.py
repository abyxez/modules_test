from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Module(models.Model):
    name = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.name
