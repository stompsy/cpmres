from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("directory/", include("directory.urls")),
    path("", RedirectView.as_view(url="directory/")),
    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    # do not do this in production
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
