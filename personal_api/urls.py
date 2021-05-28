from django.urls import path

from .views import CityWeatherView
from .views import CityForecastView
from .views import CityClothesView
from .views import CityAllInOne
from .views import AddUserFirstTime
from .views import ChangeUserPref

app_name = "all_weather"

urlpatterns = [
    path('all_in_one/lat=<lat>&lon=<lon>&user_id=<user_id>', CityAllInOne.as_view(), name='all_in_one'),
    path('weather/lat=<lat>&lon=<lon>', CityWeatherView.as_view(), name='weather_now'),
    path('weather/forecast/lat=<lat>&lon=<lon>', CityForecastView.as_view(), name='forecast'),
    path('clothes/lat=<lat>&lon=<lon>&user_id=<user_id>', CityClothesView.as_view(), name='clothes'),
    path('create_user/name=<name>&temp_pref=<temp_pref>', AddUserFirstTime.as_view(), name='add_user'),
    path('change_user/name=<name>&user_id=<user_id>&new_temp_pref=<new_temp_pref>&lat=<lat>&lon=<lon>', ChangeUserPref.as_view(), name='change_user'),
]
