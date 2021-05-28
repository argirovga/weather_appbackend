from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ordinary_functions.get_weather_data import get_current_weather_data_on_city as get_weather
from ordinary_functions.get_weather_data import get_weatherforecast_data_on_city as get_forecast
from ordinary_functions.get_weather_data import get_city_on_coord
from ordinary_functions.clothes_choice import algorithm
from ordinary_functions.registration_system import generate_token, check_access

from personal_api.models import User_preferences

import docs.build.html

from django.contrib.auth.models import User


class CityWeatherView(APIView):
    """
    Гет запрос на получение данных о погоде на данный момент по координатам

    :param request: не используется
    :param lat: широта
    :param lon: долгота

    :return: словарь из данных о погоде по полученным координатам
    """
    def get(self, request, lat, lon):

        return Response({f"weather_in_city": get_weather(float(lat), float(lon))})


class CityForecastView(APIView):
    """
    Гет запрос на получение прогноза погода по координатам

    :param request: не используется
    :param lat: широта
    :param lon: долгота

    :return: словарь из прогноза погоды по полученным координатам
    """
    def get(self, request, lat, lon):
        forecast_date = get_forecast(lat, lon)

        return Response({f"specific_forecast_data_in_city": forecast_date})


class CityClothesView(APIView):
    """
    Гет запрос на получение рекомендации по одежде по координатам

    :param request: не используется
    :param lat: широта
    :param lon: долгота
    :param user_id: уникальный токен пользователя

    :return: список рекомендованных вещей
    """
    def get(self, request, lat, lon, user_id):
        clothes_data = algorithm(lat, lon, user_id)

        return Response({f"specific_clothes_data_in_city": clothes_data})


class CityAllInOne(APIView):
    """
    Гет запрос на получение всех возможных данных по данным координатам

    :param request: не используется
    :param lat: широта
    :param lon: долгота
    :param user_id: уникальный токен пользователя

    :return: словарь из всех возможных данных(погода + одежда)
    """
    def get(self, request, lat, lon, user_id):
        data = get_weather(lat, lon)
        data['mas_clothes'] = algorithm(lat, lon, user_id)
        return Response({f"specific_all_data_in_city": data})


class AddUserFirstTime(APIView):
    """
    Гет запрос на создание нового пользователя

    :param request: не используется
    :param name: имя пользователя
    :param temp_pref: предпочтения

    :return: ответ на запрос создания нового пользователя
    """
    def get(self, request, name, temp_pref):
        user_id = generate_token()
        user = User_preferences(user_id=user_id, temp_pref=temp_pref, name=name)
        user.save()
        return Response({"success: uder_id": user_id})


class ChangeUserPref(APIView):
    """
    Гет запрос на  нового пользователя

    :param request: не используется
    :param user_id: уникальный токен пользователя
    :param name: имя пользователя
    :param new_temp_pref: новое предпочтение пользователя

    :return: ответ на запрос изменения предпочтений пользователя
    """
    def get(self, request, user_id, name, new_temp_pref, lat, lon):
        check = check_access(user_id, name)
        if check:
            templ = User_preferences.objects.get(user_id=user_id, name=name)
            templ.temp_pref = new_temp_pref
            templ.last_temp = get_weather(lat, lon)['temp']
            templ.last_hum = get_weather(lat, lon)['humidity']
            templ.save()
            return Response("success: User preference changed successfully")
        if not check:
            return Response("declined")


def view_available_requests(request):
    """
    Отображение возможных запросов

    :param request: не используется

    :return: main.html
    """
    return render(request, 'main.html')


def view_documentation(request):
    """
    Отображение документации

    :param request: не используется

    :return: index.html
    """
    return render(request, 'index.html')
