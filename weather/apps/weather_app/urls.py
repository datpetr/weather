from django.urls import path
from . import views
from .db_weather import 

app_name = 'weather_app'

urlpatterns = [
    path('', views.index, name='index'),
]
