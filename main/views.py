from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, str] = {"tittle": "Home", "content": "Main Page Home"}
    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("About us")
