from django.db import models
from django.urls import reverse
from core import models as core_models


class Business(core_models.TimeStampedModel):

    """ Business Model Definition """

    STATE_ACT = "ACT"
    STATE_NSW = "NSW"
    STATE_NT = "NT"
    STATE_QLD = "QLD"
    STATE_SA = "SA"
    STATE_TAS = "TAS"
    STATE_VIC = "VIC"
    STATE_WA = "WA"
    STATE_CHOICES = (
        (STATE_ACT, "Australian Capital Territory"),
        (STATE_NSW, "New South Wales"),
        (STATE_NT, "Northern Territory"),
        (STATE_QLD, "Queensland"),
        (STATE_SA, "South Australia"),
        (STATE_TAS, "Tasmania"),
        (STATE_VIC, "Victoria"),
        (STATE_WA, "Western Australia"),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default="NSW")
    address = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(
        "users.User", related_name="businesses", on_delete=models.CASCADE,
    )
    avatar = models.ImageField(upload_to="business_photo", null=True, blank=True)

    class Meta:
        verbose_name_plural = "businesses"

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        total_rating = 0

        if all_reviews.count() > 0:
            for review in all_reviews:
                total_rating += review.rating_average()
            return round(total_rating / len(all_reviews), 2)
        return "0"

    total_rating.short_description = "Avg"

    def get_absolute_url(self):
        return reverse("businesses:profile", kwargs={"pk": self.pk})
