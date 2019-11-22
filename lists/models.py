from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    menu = models.ManyToManyField("menus.Menu", blank=True)

    def __str__(self):
        date = self.created.date()
        format_date = date.strftime("%Y/%m/%d")
        return f"{format_date} / {self.user}"

    def count_menus(self):
        return self.menu.count()

    count_menus.short_description = "Menu Number"
