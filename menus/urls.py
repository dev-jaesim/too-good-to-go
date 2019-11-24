from django.urls import path
from . import views


app_name = "menus"

urlpatterns = [
    path("<int:pk>/", views.MenuDetail.as_view(), name="detail"),
]
