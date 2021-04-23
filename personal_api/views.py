from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ordinary_functions.get_weather_data import get_current_weather_data_on_city as get_weather
from ordinary_functions.get_weather_data import get_weatherforecast_data_on_city as get_forecast
from ordinary_functions.clothes_choice import weather_choice_mech as get_clothes, bolvanka
from ordinary_functions.get_weather_data import get_city_on_coord

from django.contrib.auth.models import User


class CityWeatherView(APIView):
    def get(self, request, lat, lon):
        city = get_city_on_coord(float(lat), float(lon))
        return Response({f"weather_in_{city}": get_weather(float(lat), float(lon))})


class CityForecastView(APIView):
    def get(self, request, lat, lon):
        city = get_city_on_coord(float(lat), float(lon))
        forecast_date = get_forecast(lat, lon)

        return Response({f"specific_forecast_data_in_{city}": forecast_date})


class CityClothesView(APIView):
    def get(self, request, lat, lon):
        city = get_city_on_coord(float(lat), float(lon))
        clothes_data = get_clothes(lat, lon)
        return Response({f"specific_clothes_data_in_{city}": clothes_data})


class CityAllInOne(APIView):
    def get(self, request, lat, lon):
        data = bolvanka(get_weather(lat, lon))
        city = get_city_on_coord(float(lat), float(lon))
        return Response({f"specific_all_data_in_{city}": data})


class AddUser(APIView):
    def post(self, request):
        user = request.data.get('User_info')

        # Create an article from the above data
        new_user = User.objects.create_user(username=user['username'], email=user['email'], password=user['password'])
        new_user.save()
        return Response("success: User created successfully")


'''
{
    "User_info": {
        "username": "vasya_228"
        "email": "vasya_228@gmail.com"
        "password": "228"
    }
}
'''


def view_available_requests(request):
    return render(request, 'main.html')
