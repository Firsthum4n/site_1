from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, '')


def about(request):
    return HttpResponse("<h4>Страница про нас</h4>")


def contacts(request):
    return HttpResponse("<h4>контакты: 8123132311, 8349305483</h4>")
