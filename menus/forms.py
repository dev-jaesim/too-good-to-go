from django import forms
from . import models


class SearchForm(forms.Form):

    STATE_ACT = "ACT"
    STATE_NSW = "NSW"
    STATE_NT = "NT"
    STATE_QLD = "QLD"
    STATE_SA = "SA"
    STATE_TAS = "TAS"
    STATE_VIC = "VIC"
    STATE_WA = "WA"
    STATE_FIRST = "None"
    STATE_CHOICES = (
        (STATE_FIRST, "Anywhere"),
        (STATE_ACT, "Australian Capital Territory"),
        (STATE_NSW, "New South Wales"),
        (STATE_NT, "Northern Territory"),
        (STATE_QLD, "Queensland"),
        (STATE_SA, "South Australia"),
        (STATE_TAS, "Tasmania"),
        (STATE_VIC, "Victoria"),
        (STATE_WA, "Western Australia"),
    )

    state = forms.ChoiceField(choices=STATE_CHOICES)
    food_type = forms.ModelChoiceField(
        required=False,
        empty_label="Any kind",
        queryset=models.FoodType.objects.all(),
        label="Food Type",
    )


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("caption", "file")

    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        menu = models.Menu.objects.get(pk=pk)
        photo.menu = menu
        photo.save()
