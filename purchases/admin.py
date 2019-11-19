from django.contrib import admin
from . import models


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "status",
        "purchase_date",
        "user",
        "menu",
        "business",
        "price",
    )

    list_filter = (
        "user",
        "menu",
    )
