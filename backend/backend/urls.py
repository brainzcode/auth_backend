from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("djoser.urls")),
    path("api/", include("users.urls")),
    path("api/properties/", include("properties.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
