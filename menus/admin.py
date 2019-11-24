from django.contrib import admin
from django.utils.html import mark_safe
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

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):

    """ Menu Admin Definition """

    inlines = (PhotoInline,)

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
        "count_photos",
        "in_progress",
    )

    list_filter = ("food_type",)

    # raw_id_fields = ("business",)

    filter_horizontal = ("food_type",)

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photos"
