from django.urls import path

from django_blog.core.views import index, privacy, terms

app_name = "core"
urlpatterns = [
    path("index/", view=index, name="index"),
    path("terms/", view=terms, name="terms"),
    path("privacy/", view=privacy, name="privacy"),
]
