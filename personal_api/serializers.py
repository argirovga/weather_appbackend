from rest_framework import serializers
from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
import datetime

User = get_user_model()


class WeatherDataSerializer(serializers.Serializer):
    """
    Отображение данных погоды для наглядного представления
    """
    city_name = serializers.CharField(max_length=100)
    main = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=300)
    temp = serializers.IntegerField()
    temp_min = serializers.IntegerField()
    temp_max = serializers.IntegerField()
    feels_like = serializers.IntegerField()
    pressure = serializers.IntegerField()
    humidity = serializers.IntegerField()
    wind_speed = serializers.IntegerField()
    warning = serializers.CharField(max_length=500)
    date = serializers.DateField(default=date.today)
    time = serializers.TimeField(default=datetime.datetime.now().time())

