from django.views.generic import FormView
from django.shortcuts import reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from users import mixins as user_mixins
from . import forms
from businesses import models as business_model


class CreateReviewView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, FormView):

    """ CreateReviewView Definition """

    template_name = "reviews/review_create.html"
    form_class = forms.CreateReviewForm
    success_message = "Review Uploaded"

    def form_valid(self, form):
        review = form.save()
        business_pk = self.kwargs.get("pk")
        review.business = business_model.Business.objects.get(pk=business_pk)
        review.user = self.request.user
        review.save()
        return redirect(reverse("businesses:profile", kwargs={"pk": business_pk}))
