"""
URL configuration for project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django_blog.core.views import index

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    path("", view=index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
