from django.views.generic import ListView
from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from menus import models as menu_models
from users import mixins


class ListDetailView(ListView, mixins.LoggedInOnlyView):

    """ HistoryView Definition """

    model = models.List
    paginate_by = 10
    paginate_orphans = 3
    context_object_name = "lists"

    def get_queryset(self):
        return models.List.objects.filter(user=self.request.user)


class CreateError(Exception):
    pass


@login_required
def addToMyList(request, pk):
    try:
        models.List.objects.get(user=request.user, menu=pk)
        raise CreateError()
    except (CreateError):
        messages.error(request, "You already have this menu in your list")
        return redirect(reverse("menus:detail", kwargs={"pk": pk}))
    except models.List.DoesNotExist:
        menu = menu_models.Menu.objects.get(pk=pk)
        models.List.objects.create(
            user=request.user, menu=menu,
        )
        return redirect(reverse("lists:list-detail"))


@login_required
def deleteItem(request, pk):
    models.List.objects.filter(pk=pk).delete()
    return redirect(reverse("lists:list-detail"))
