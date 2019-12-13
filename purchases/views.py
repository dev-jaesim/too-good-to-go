from django.views.generic import ListView
from django.shortcuts import redirect, reverse
from django.contrib.auth.decorators import login_required
from . import models
from menus import models as menu_models
from users import mixins


class HistoryView(ListView, mixins.LoggedInOnlyView):

    """ HistoryView Definition """

    model = models.Purchase
    paginate_by = 5
    paginate_orphans = 3
    context_object_name = "purchases"

    def get_queryset(self):
        return models.Purchase.objects.filter(user=self.request.user)


@login_required
def create(request, pk):
    menu = menu_models.Menu.objects.get(pk=pk)
    stock = menu.stock
    models.Purchase.objects.create(
        user=request.user, menu=menu,
    )
    menu_models.Menu.objects.filter(pk=pk).update(stock=stock - 1)
    return redirect(reverse("purchases:history"))
