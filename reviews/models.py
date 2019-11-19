from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    taste = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    portion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    location = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    business = models.ForeignKey(
        "businesses.Business", related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.business} / {self.user.first_name} {self.user.last_name}"

    def rating_average(self):
        avg = (self.taste + self.portion + self.value + self.location) / 4
        return round(avg, 2)

    rating_average.short_description = "Avg"
