from django.urls import path

from .views import CityWeatherView
from .views import CityForecastView
from .views import CityClothesView
from .views import CityAllInOne
from .views import AddUser

app_name = "all_weather"

urlpatterns = [
    path('all_in_one/city=<str:city>', CityAllInOne.as_view()),
    path('weather/city=<str:city>', CityWeatherView.as_view()),
    path('weather/forecast/city=<str:city>', CityForecastView.as_view()),
    path('clothes/city=<str:city>', CityClothesView.as_view()),
    path('create_user/', AddUser.as_view()),
]
