from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from src.apps.common.views import redirect_to_admin

urlpatterns = [
    path("", redirect_to_admin),
    path("admin/", admin.site.urls),
    path("customer-supports/", include("src.apps.CustomerSupport.urls")),
    path("users/", include("src.apps.users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
