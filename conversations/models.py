from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    menu_owner = models.ForeignKey(
        "users.User",
        related_name="conversasions_menu_owner",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    asking_user = models.ForeignKey(
        "users.User",
        related_name="conversasions_asking_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        usernames = [self.menu_owner.first_name, self.asking_user.first_name]
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"

