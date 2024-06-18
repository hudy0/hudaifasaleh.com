"""
URL configuration for project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path("accounts/", include("allauth.urls")),
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    path("", include("django_blog.home.urls")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
