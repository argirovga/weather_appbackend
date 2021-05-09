import datetime

from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()


class Weather_data(models.Model):
    city_name = models.CharField(max_length=100)
    main = models.CharField(max_length=300, default='None')
    description = models.CharField(max_length=300, default='None')
    temp = models.IntegerField()
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    feels_like = models.IntegerField()
    pressure = models.IntegerField()
    humidity = models.IntegerField()
    wind_speed = models.IntegerField()
    warning = models.CharField(max_length=500, default='clear')
    date = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.datetime.now().time())

    def __str__(self):
        return self.city_name


class User_preferences(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    temp_pref = models.IntegerField()
    wind_pref = models.IntegerField()
    fall_out_pref = models.IntegerField()

    def __str__(self):
        return self.user

