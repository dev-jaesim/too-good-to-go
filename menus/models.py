from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class FoodType(AbstractItem):

    """ FoodType Model Definition """

    class Meta:
        verbose_name = "Food Type"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="food_photos")
    menu = models.ForeignKey(
        "Menu", related_name="photos", on_delete=models.CASCADE, blank=True
    )

    def __str__(self):
        return self.caption


class Menu(core_models.TimeStampedModel):

    """ Menu Model Definition """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0)],
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(500)],
    )
    business = models.ForeignKey(
        "businesses.Business", related_name="menus", on_delete=models.CASCADE,
    )
    food_type = models.ManyToManyField("FoodType", related_name="menus", blank=True)

    def __str__(self):
        return self.name

    def in_progress(self):
        today = timezone.now().date()
        return self.stock > 0 and self.created.date() == today

    in_progress.boolean = True
