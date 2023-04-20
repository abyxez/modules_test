from django.contrib import admin

from .models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "description",
        "created",
    )
    list_editable = (
        "description",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("created",)
    empty_value_display = "-пусто-"
