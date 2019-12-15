from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):

    taste = forms.IntegerField(max_value=5, min_value=1)
    portion = forms.IntegerField(max_value=5, min_value=1)
    value = forms.IntegerField(max_value=5, min_value=1)
    location = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "review",
            "taste",
            "portion",
            "value",
            "location",
        )

    def save(self, *args, **kwargs):
        review = super().save(commit=False)
        return review
