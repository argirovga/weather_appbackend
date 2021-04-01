from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ordinary_functions.get_weather_data import get_current_weather_data_on_city as get_weather
from ordinary_functions.get_weather_data import get_weatherforecast_data_on_city as get_forecast
from ordinary_functions.weather_choice import weather_choice_mech as get_clothes


from .models import Weather_data
from .models import Clothes_recommendation
from .serializers import WeatherDataSerializer
from .serializers import ClothesRecommendationSerializer

from django.contrib.auth.models import User

from datetime import date
import datetime


class CityWeatherView(APIView):
    def get(self, request, city):
        yesterday_date = date.today()-datetime.timedelta(days=1)
        exist = False
        filtered_data = Weather_data.objects.filter(city_name=city)
        if city in Weather_data.objects.values_list('city_name', flat=True):
            exist = True

        if yesterday_date in Weather_data.objects.values_list('date', flat=True):
            instance = Weather_data.objects.get(date=yesterday_date)
            instance.delete()

        if not exist:
            print('noah')
            weather_data = get_weather(city)
            new_obj_weath = Weather_data(city_name=weather_data['city_name'], temp=weather_data['temp'],
                                         temp_min=weather_data['temp_min'],
                                         temp_max=weather_data['temp_max'], feels_like=weather_data['feels_like'],
                                         pressure=weather_data['pressure'],
                                         humidity=weather_data['humidity'], wind_speed=weather_data['wind_speed'],
                                         date=date.today())
            new_obj_weath.save()
            return Response({"specific_city_weather_data": weather_data})
        if exist:
            print("YEAH")
            serializer = WeatherDataSerializer(filtered_data[0])

            return Response({"weather_database": serializer.data})


class CityForecastView(APIView):
    def get(self, request, city):
        forecast_date = get_forecast(city)

        return Response({"specific_city_forecast_data": forecast_date})


class CityClothesView(APIView):
    def get(self, request, city):
        clothes_data = get_clothes(get_weather(city))

        return Response({"specific_city_clothes_data": clothes_data})


class AddUser(APIView):
    def post(self, request):
        user = request.data.get('User_info')

        # Create an article from the above data
        new_user = User.objects.create_user(username=user['username'], email=user['email'], password=user['password'])
        new_user.save()
        return Response("success: User  created successfully")


'''
{
    "User_info": {
        "username": "vasya_228"
        "email": "vasya_228@gmail.com"
        "password": "228"
    }
}
'''
