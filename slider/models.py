from django.db import models
from core import models as core_models


class Slider(core_models.TimeStampedModel):

    """ Slider Model Definition """

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="slider_photos")

    def __str__(self):
        return self.caption
