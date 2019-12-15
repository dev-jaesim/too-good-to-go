from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, reverse, render
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from users import models as user_models
from . import models
from users import mixins


@login_required
def go_conversation(request, menu_owner_pk, asking_user_pk):
    try:
        menu_owner = user_models.User.objects.get(pk=menu_owner_pk)
    except menu_owner.DoesNotExist:
        menu_owner = None

    try:
        asking_user = user_models.User.objects.get(pk=asking_user_pk)
    except asking_user.DoesNotExist:
        asking_user = None

    try:
        conversation = models.Conversation.objects.get(
            menu_owner=menu_owner, asking_user=asking_user
        )
    except models.Conversation.DoesNotExist:
        conversation = models.Conversation.objects.create(
            asking_user=asking_user, menu_owner=menu_owner
        )
    return redirect(reverse("conversations:detail", kwargs={"pk": conversation.pk}))


class ConversationDetailView(View, mixins.LoggedInOnlyView):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        return render(
            self.request,
            "conversations/conversation_detail.html",
            {"conversation": conversation},
        )

    def post(self, *args, **kwargs):
        message = self.request.POST.get("message", None)
        pk = kwargs.get("pk")
        conversation = models.Conversation.objects.get_or_none(pk=pk)
        if not conversation:
            raise Http404()
        if message is not None:
            models.Message.objects.create(
                message=message, user=self.request.user, conversation=conversation
            )
        return redirect(reverse("conversations:detail", kwargs={"pk": pk}))


class ConversationView(ListView, mixins.LoggedInOnlyView):

    """ ConversationView Definition """

    model = models.Conversation
    paginate_by = 10
    paginate_orphans = 3
    context_object_name = "conversations"

    def get_queryset(self):
        return models.Conversation.objects.filter(
            Q(asking_user=self.request.user) | Q(menu_owner=self.request.user)
        )
