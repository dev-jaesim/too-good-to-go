from django.db import models
from django.urls import reverse
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
        "businesses.Business", related_name="menus", on_delete=models.CASCADE, null=True
    )
    food_type = models.ManyToManyField("FoodType", related_name="menus", blank=True)

    def __str__(self):
        return self.name

    def in_progress(self):
        today = timezone.now().date()
        return self.stock > 0 and self.created.date() == today

    in_progress.boolean = True

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos

    def get_absolute_url(self):
        return reverse("menus:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0
