from django.contrib import admin
from . import models


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {"fields": ("name", "description",)},),
        ("Address", {"fields": ("state", "address",)}),
        ("Other", {"fields": ("owner", "avatar",)}),
    )

    list_display = ("name", "state", "address", "owner", "total_rating")

    search_fields = ("^name", "^owner__username")
