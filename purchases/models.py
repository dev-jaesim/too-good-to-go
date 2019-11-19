from datetime import datetime
from django.db import models
from core import models as core_models


class Purchase(core_models.TimeStampedModel):

    """ Purchase Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    user = models.ForeignKey(
        "users.User", related_name="purchases", on_delete=models.CASCADE
    )

    menu = models.ForeignKey(
        "menus.Menu", related_name="purchases", on_delete=models.CASCADE
    )

    business = models.ForeignKey(
        "businesses.Business",
        related_name="purchases",
        on_delete=models.CASCADE,
        blank=True,
    )

    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True,)

    def purchase_date(self):
        date = self.created.date()
        format_date = date.strftime("%Y/%m/%d")
        return format_date

    purchase_date.short_description = "Date"

    def save(self, *args, **kwargs):
        self.business = self.menu.business
        self.price = self.menu.price
        super().save(*args, **kwargs)

