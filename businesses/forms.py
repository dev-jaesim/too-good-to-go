from django import forms
from . import models


class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = models.Business
        fields = (
            "name",
            "description",
            "state",
            "address",
            "avatar",
        )

    def save(self, *args, **kwargs):
        business = super().save(commit=False)
        return business
