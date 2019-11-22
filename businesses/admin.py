from django.contrib import admin
from . import models


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "address", "owner", "total_rating")

    search_fields = ("^name", "^owner__username")
