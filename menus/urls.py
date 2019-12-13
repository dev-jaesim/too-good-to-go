from django.urls import path
from . import views


app_name = "menus"

urlpatterns = [
    path("<int:pk>/", views.MenuDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("update-menu/<int:pk>", views.UpdateMenuView.as_view(), name="update-menu"),
    path("<int:pk>/photos/", views.MenuPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add", views.AddPhotoView.as_view(), name="add-photo"),
    path(
        "<int:menu_pk>/photos/<int:photo_pk>/edit/",
        views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path(
        "<int:menu_pk>/photos/<int:photo_pk>/delete/",
        views.delete_photo,
        name="delete-photo",
    ),
    path("create/<int:business_pk>", views.CreateMenuView.as_view(), name="create"),
]
