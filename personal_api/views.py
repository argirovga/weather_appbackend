from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ordinary_functions.get_weather_data import get_current_weather_data_on_city as get_weather
from ordinary_functions.get_weather_data import get_weatherforecast_data_on_city as get_forecast
from ordinary_functions.get_weather_data import get_city_on_coord
from ordinary_functions.clothes_choice import algorithm
from ordinary_functions.registration_system import generate_token, check_access

from personal_api.models import User_preferences

from django.contrib.auth.models import User


class CityWeatherView(APIView):
    def get(self, request, lat, lon):
        city = get_city_on_coord(float(lat), float(lon))
        return Response({f"weather_in_city": get_weather(float(lat), float(lon))})


class CityForecastView(APIView):
    def get(self, request, lat, lon):
        city = get_city_on_coord(float(lat), float(lon))
        forecast_date = get_forecast(lat, lon)

        return Response({f"specific_forecast_data_in_city": forecast_date})


class CityClothesView(APIView):
    def get(self, request, lat, lon):
        city = get_city_on_coord(float(lat), float(lon))
        clothes_data = algorithm(lat, lon)
        return Response({f"specific_clothes_data_in_city": clothes_data})


class CityAllInOne(APIView):
    def get(self, request, lat, lon):
        data = get_weather(lat, lon)
        data['mas_clothes'] = algorithm(lat, lon)
        city = get_city_on_coord(float(lat), float(lon))
        return Response({f"specific_all_data_in_city": data})


class AddUserFirstTime(APIView):
    def get(self, request, name, temp_pref):
        user_id = generate_token()
        user = User_preferences(user_id=user_id, temp_pref=temp_pref, name=name)
        user.save()
        return Response({"success: uder_id" : user_id})


class ChangeUserPref(APIView):
    def get(self, request, user_id, name, new_temp_pref):
        check = check_access(user_id, name)
        if check:
            templ = User_preferences.objects.get(user_id=user_id, name=name)
            templ.temp_pref = new_temp_pref
            templ.save()
            return Response("success: User preference changed successfully")
        if not check:
            return Response("declined")


def view_available_requests(request):
    return render(request, 'main.html')
