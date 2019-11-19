from django.contrib import admin
from . import models


@admin.register(models.FoodType)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.menus.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):

    """ Menu Admin Definition """

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "price", "stock",)},),
        ("Provided by", {"fields": ("business",)}),
        ("Food Type", {"fields": ("food_type",)}),
    )

    list_display = (
        "name",
        "description",
        "price",
        "stock",
        "business",
    )

    list_filter = (
        "price",
        "stock",
        "food_type",
    )

    raw_id_fields = ("business",)

    filter_horizontal = ("food_type",)
