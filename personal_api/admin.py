from django.contrib import admin

from .models import Weather_data, User_preferences


admin.site.register(Weather_data)
admin.site.register(User_preferences)