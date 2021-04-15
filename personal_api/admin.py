from django.contrib import admin

from .models import Weather_data, Clothes_recommendation, User_preferences


admin.site.register(Weather_data)
admin.site.register(Clothes_recommendation)
admin.site.register(User_preferences)