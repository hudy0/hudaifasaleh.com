from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """
    The entry point of the application.
    """
    return render(request, "core/index.html", {})
