from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная стираница',
        'values': ['some', 'hello', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


