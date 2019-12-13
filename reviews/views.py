from django.http import Http404
from django.views.generic import View, ListView, DetailView, UpdateView, FormView
from django.shortcuts import render, reverse, redirect
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users import mixins as user_mixins
from . import models, forms
from businesses import models as business_model
from slider import models as slider_models


class CreateReviewView(user_mixins.LoggedInOnlyView, FormView):

    """ CreateReviewView Definition """

    template_name = "menus/photo_create.html"
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("menus:photos", kwargs={"pk": pk}))
