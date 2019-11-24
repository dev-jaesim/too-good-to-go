from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Menu
    paginate_by = 5
    # paginate_orphans = 3
    context_object_name = "menus"
    # user_state = "ACT"

    # def get_queryset(self):
    #     return models.Menu.objects.filter(business__state=self.user_state)


class MenuDetail(DetailView):

    """ MenuDetail Definition """

    model = models.Menu
