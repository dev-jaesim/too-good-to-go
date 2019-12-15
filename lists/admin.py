from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    # list_display = ("__str__", "count_menus")

    list_filter = ("user",)

    raw_id_fields = ("user",)

    # filter_horizontal = ("menu",)
