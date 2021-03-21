from django.urls import path
from . import views


app_name = 'weather_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('diamond/', views.diamond_, name='diamond_'),
    path('forest/', views.forest_, name='forest_'),
    path('garden/', views.garden_, name='garden_'),
    path('northern/', views.northern_, name='northern_'),
    path('polar/', views.polar_, name='polar_'),
    path('scientific/', views.scientific_, name='scientific_'),
    path('seaside/', views.seaside_, name='seaside_'),
    path('south/', views.south_, name='south_'),
    path('stepnoy/', views.stepnoy_, name='stepnoy_'),
    path('taiga/', views.taiga_, name='taiga_'),
    path('western/', views.western_, name='western_'),
    path('polar_city/', views.polar_city_, name='polar_city_'),
    path('resort/', views.resort_, name='resort_'),
]
