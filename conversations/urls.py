from django.urls import path
from . import views

app_name = "conversations"

urlpatterns = [
    path(
        "go/<int:menu_owner_pk>/<int:asking_user_pk>", views.go_conversation, name="go"
    ),
    path("<int:pk>/", views.ConversationDetailView.as_view(), name="detail"),
    path("", views.ConversationView.as_view(), name="all-conversations"),
]
