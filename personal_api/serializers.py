from rest_framework import serializers
from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
User = get_user_model()


class WeatherDataSerializer(serializers.Serializer):
    city_name = serializers.CharField(max_length=100)
    temp = serializers.IntegerField()
    temp_min = serializers.IntegerField()
    temp_max = serializers.IntegerField()
    feels_like = serializers.IntegerField()
    pressure = serializers.IntegerField()
    humidity = serializers.IntegerField()
    wind_speed = serializers.IntegerField()
    date = serializers.DateField(default=date.today)


class ClothesRecommendationSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    main_description = serializers.CharField(max_length=600)
    need_umbrella = serializers.BooleanField()
    type_of_hat = serializers.CharField(max_length=100)
    data = serializers.DateField(default=date.today())
