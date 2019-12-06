from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("menus/", include("menus.urls", namespace="menus")),
    path("users/", include("users.urls", namespace="users")),
    path("businesses/", include("businesses.urls", namespace="businesses")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
