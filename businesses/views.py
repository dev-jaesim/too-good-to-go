from django.http import Http404
from django.views.generic import DetailView, UpdateView
from . import models


class BusinessProfileView(DetailView):

    """ BusinessProfileView Definition """

    model = models.Business
    context_object_name = "business_obj"


class UpdateBusinessProfileView(UpdateView):

    """ UpdateBusinessProfileView Definition """

    model = models.Business
    template_name = "businesses/update-business-profile.html"
    fields = (
        "name",
        "description",
        "state",
    )
    success_message = "Profile Updated"

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        business = super().get_object(queryset=queryset)
        if business.owner.pk != self.request.user.pk:
            raise Http404()
        return business

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["name"].widget.attrs = {"placeholder": "Name"}
        form.fields["description"].widget.attrs = {"placeholder": "Description"}
        return form
