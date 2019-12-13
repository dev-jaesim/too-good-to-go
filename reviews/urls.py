from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [
    path("<int:pk>/", views.CreateReviewView.as_view(), name="create-review"),
]
