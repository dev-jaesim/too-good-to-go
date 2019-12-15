from django.urls import path
from . import views


app_name = "lists"

urlpatterns = [
    path("", views.ListDetailView.as_view(), name="list-detail"),
    path("add/<int:pk>", views.addToMyList, name="add-to-list"),
    path("delete/<int:pk>", views.deleteItem, name="delete-item"),
]
