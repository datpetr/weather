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
    return render(request, 'weather_app/test.html')


def forest_(request):
    return render(request, 'weather_app/forest.html')


def garden_(request):
    return render(request, 'weather_app/garden.html')


def northern_(request):
    return render(request, 'weather_app/northern.html')


def polar_(request):
    return render(request, 'weather_app/polar.html')


def resort_(request):
    return render(request, 'weather_app/resort.html')


def scientific_(request):
    return render(request, 'weather_app/scientific.html')


def seaside_(request):
    return render(request, 'weather_app/seaside.html')


def south_(request):
    return render(request, 'weather_app/south.html')


def stepnoy_(request):
    return render(request, 'weather_app/stepnoy.html')


def taiga_(request):
    return render(request, 'weather_app/taiga.html')


def western_(request):
    return render(request, 'weather_app/western.html')


def polar_city_(request):
    return render(request, 'weather_app/polar_city.html')
