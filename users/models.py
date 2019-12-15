import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.urls import reverse

# from core import managers as core_managers


class User(AbstractUser):

    """ Custom User Model """

    STATE_ACT = "ACT"
    STATE_NSW = "NSW"
    STATE_NT = "NT"
    STATE_QLD = "QLD"
    STATE_SA = "SA"
    STATE_TAS = "TAS"
    STATE_VIC = "VIC"
    STATE_WA = "WA"
    STATE_CHOICES = (
        (STATE_ACT, "Australian Capital Territory"),
        (STATE_NSW, "New South Wales"),
        (STATE_NT, "Northern Territory"),
        (STATE_QLD, "Queensland"),
        (STATE_SA, "South Australia"),
        (STATE_TAS, "Tasmania"),
        (STATE_VIC, "Victoria"),
        (STATE_WA, "Western Australia"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
    )

    state = models.CharField(max_length=50, choices=STATE_CHOICES, default="NSW")
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    business_owner = models.BooleanField(default=False)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default="email"
    )
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    # objects = core_managers.CustomModelManager()

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Too Good To Go Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
