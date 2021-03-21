from django.shortcuts import render
from django.http import HttpResponse
from .db_weather import diamond, \
    forest, garden, northern, \
    polar, port_city, \
    resort, scientific, \
    seaside, south, \
    stepnoy, taiga, western

# Create your views here.


def index(request):
    return HttpResponse('test')


def diamond_(request):
    return render(request, 'test.html')


def forest_(request):
    return render(request, 'forest.html')


def garden_(request):
    return render(request, 'garden.html')


def northern_(request):
    return render(request, 'northern.html')


def polar_(request):
    return render(request, 'polar.html')


def resort_(request):
    return render(request, 'resort.html')


def scientific_(request):
    return render(request, 'scientific.html')


def seaside_(request):
    return render(request, 'seaside.html')


def south_(request):
    return render(request, 'south.html')


def stepnoy_(request):
    return render(request, 'stepnoy.html')


def taiga_(request):
    return render(request, 'taiga.html')


def western_(request):
    return render(request, 'western.html')


def polar_city_(request):
    return render(request, 'polar_city.html')
