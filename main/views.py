from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    context: dict[str, str] = {
        "tittle": "Home",
        "content": "Main Page Home",
    }
    return render(request, 'main/index.html', context)


def about(request: HttpRequest) -> HttpResponse:
    context: dict[str, str] = {
        "tittle": "About us",
        "content": "About us",
        "text_on_page": "We are a very good company",
    }
    return render(request, 'main/about.html', context)
