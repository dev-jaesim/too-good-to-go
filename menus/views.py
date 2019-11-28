from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


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
