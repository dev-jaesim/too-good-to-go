from django.urls import path
from menus import views as menu_views


app_name = "core"

urlpatterns = [
    path("", menu_views.HomeView.as_view(), name="home"),
]
