from django.urls import path

from .views import CityWeatherView
from .views import CityForecastView
from .views import CityClothesView
from .views import CityAllInOne
from .views import AddUser

app_name = "all_weather"

urlpatterns = [
    path('all_in_one/lat=<lat>&lon=<lon>', CityAllInOne.as_view()),
    path('weather/lat=<lat>&lon=<lon>', CityWeatherView.as_view()),
    path('weather/forecast/lat=<lat>&lon=<lon>', CityForecastView.as_view()),
    path('clothes/lat=<lat>&lon=<lon>', CityClothesView.as_view()),
    path('create_user/', AddUser.as_view()),
]
