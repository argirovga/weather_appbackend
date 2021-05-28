import datetime

from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class Weather_data(models.Model):
    """
    Основная модель для хранение данных погоды

    :param city_name: название города
    :param main: главное описание погодных условий
    :param description: подробное описание погодных условий
    :param temp: температура
    :param temp_min: минимальная температура этим днём
    :param temp_max: максимальная температура этим днём
    :param feels_like: ощущается как
    :param pressure: давление
    :param humidity: влажность
    :param wind_speed: скорость ветра
    :param warning: предупреждение
    :param date: дата запроса с сервиса OpenWeatherMap
    :param time: время запроса с сервиса OpenWeatherMap
    """
    city_name = models.CharField(max_length=100)
    main = models.CharField(max_length=300, default='None')
    description = models.CharField(max_length=300, default='None')
    temp = models.IntegerField(default=0)
    temp_min = models.IntegerField(default=0)
    temp_max = models.IntegerField(default=0)
    feels_like = models.IntegerField(default=0)
    pressure = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    wind_speed = models.IntegerField(default=0)
    warning = models.CharField(max_length=500, default='clear')
    date = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.datetime.now().time())

    def __str__(self):
        return self.city_name


class User_preferences(models.Model):
    """
    Модель для хранение предпочтений пользователя

    :param user_id: уникальный токен пользователя
    :param temp_pref: препочтения по температуре
    :param wind_pref: восприимчивость к ветру (пока не используется)
    :param humidity_pref: восприимчивость к влажности (пока не используется)
    :param name: имя пользователя
    """
    user_id = models.CharField(max_length=300, default='0')
    temp_pref = models.IntegerField(default=0)
    wind_pref = models.IntegerField(default=0)
    humidity_pref = models.IntegerField(default=0)
    name = models.CharField(max_length=300, default=None)
    last_temp = models.IntegerField(default=-100)
    last_hum = models.IntegerField(default=-100)

    def __str__(self):
        return self.name

