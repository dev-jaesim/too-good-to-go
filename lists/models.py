from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    # menu = models.ManyToManyField("menus.Menu", blank=True)
    menu = models.ForeignKey(
        "menus.Menu",
        related_name="lists",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        date = self.created.date()
        format_date = date.strftime("%Y/%m/%d")
        return f"{format_date} / {self.user}"

    class Meta:
        ordering = ("-created",)
