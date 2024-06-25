"""
URL configuration for project.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    path("core/", include("django_blog.core.urls", namespace="core")),
]
