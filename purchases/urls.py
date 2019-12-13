from django.urls import path
from . import views

app_name = "purchases"

urlpatterns = [
    path("history/", views.HistoryView.as_view(), name="history"),
    path("order/<int:pk>", views.create, name="order"),
]
