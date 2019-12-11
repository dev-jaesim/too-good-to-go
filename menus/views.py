from django.http import Http404
from django.views.generic import View, ListView, DetailView, UpdateView, FormView
from django.shortcuts import render, reverse, redirect
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users import mixins as user_mixins
from . import models, forms
from slider import models as slider_models


class HomeView(ListView):

    """ HomeView Definition """

    logged_user = None

    model = models.Menu
    paginate_by = 5
    # paginate_orphans = 3
    context_object_name = "menus"

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return models.Menu.objects.all()

        return models.Menu.objects.filter(business__state=self.request.user.state)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["images"] = slider_models.Slider.objects.all()
        return context


class MenuDetail(DetailView):

    """ MenuDetail Definition """

    model = models.Menu


class SearchView(View):

    """ SearchView Definition """

    def get(self, request):
        state = request.GET.get("state")

        if state:
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                state = form.cleaned_data.get("state")
                food_type = form.cleaned_data.get("food_type")
                filter_args = {}

                if state != "None":
                    filter_args["business__state"] = state

                if food_type is not None:
                    filter_args["food_type"] = food_type

                qs = models.Menu.objects.filter(**filter_args).order_by("-created")
                paginator = Paginator(qs, 5, orphans=2)
                page = request.GET.get("page", 1)
                menus = paginator.get_page(page)

                return render(
                    request, "menus/search.html", {"form": form, "menus": menus}
                )

        else:
            form = forms.SearchForm()

        return render(request, "menus/search.html", {"form": form})


class UpdateMenuView(UpdateView):

    """ UpdateMenuView Definition """

    model = models.Menu
    template_name = "menus/update-menu.html"
    fields = ("name", "description", "price", "stock", "food_type")
    success_message = "Profile Updated"

    def get_object(self, queryset=None):
        menu = super().get_object(queryset=queryset)
        if menu.business.owner.pk != self.request.user.pk:
            raise Http404()
        return menu

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["name"].widget.attrs = {"placeholder": "Name"}
        form.fields["description"].widget.attrs = {"placeholder": "Description"}
        form.fields["price"].widget.attrs = {"placeholder": "price"}
        form.fields["stock"].widget.attrs = {"placeholder": "stock"}
        form.fields["food_type"].widget.attrs = {"placeholder": "food_type"}
        return form


class MenuPhotosView(user_mixins.LoggedInOnlyView, DetailView):

    """ MenuPhotosView Definition """

    model = models.Menu
    template_name = "menus/menu_photos.html"

    def get_object(self, queryset=None):
        menu = super().get_object(queryset=queryset)
        if menu.business.owner.pk != self.request.user.pk:
            raise Http404()
        return menu


class AddPhotoView(user_mixins.LoggedInOnlyView, FormView):

    """ AddPhotoView Definition """

    template_name = "menus/photo_create.html"
    form_class = forms.CreatePhotoForm

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        form.save(pk)
        messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("menus:photos", kwargs={"pk": pk}))


class EditPhotoView(user_mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):

    """ EditPhotoView Definition """

    model = models.Photo
    template_name = "menus/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("caption",)

    def get_success_url(self):
        menu_pk = self.kwargs.get("menu_pk")
        return reverse("menus:photos", kwargs={"pk": menu_pk})


@login_required
def delete_photo(request, menu_pk, photo_pk):
    user = request.user
    try:
        menu = models.Menu.objects.get(pk=menu_pk)
        if menu.business.owner.pk != user.pk:
            messages.error(request, "Cant delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            messages.success(request, "Photo Deleted")
        return redirect(reverse("menus:photos", kwargs={"pk": menu_pk}))
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
