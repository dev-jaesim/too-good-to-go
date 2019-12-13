from django.urls import path
from . import views

app_name = "businesses"

urlpatterns = [
    path("<int:pk>/", views.BusinessProfileView.as_view(), name="profile"),
    path(
        "update-business-profile/<int:pk>",
        views.UpdateBusinessProfileView.as_view(),
        name="update-business",
    ),
    path("create/", views.CreateBusinessView.as_view(), name="create"),
]
