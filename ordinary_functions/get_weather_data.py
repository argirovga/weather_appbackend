import requests
from datetime import date
import datetime
from geopy import Nominatim

from personal_api.serializers import WeatherDataSerializer

from personal_api.models import Weather_data


def clear_old_weather_on_data():
    for i in Weather_data.objects.values_list('date', flat=True):
        if str(i) != str(date.today()):
            Weather_data.objects.filter(date=i).delete()


def clear_old_weather_on_time():
    now = datetime.datetime.now().time()

    for i in Weather_data.objects.values_list('time', flat=True):
        if i < now.replace(hour=now.hour - 1):
            Weather_data.objects.filter(time=i).delete()


def warning_priority(mas):
    res = str()
    for i in mas:
        if i == 'tornado':
            res = i
            break
        if i == 'squalls':
            res = i
            break
        if i == 'thunderstorm':
            res = i
            break
        if i == 'dust':
            res = i
            break
        if i == 'rain' or i == 'snow':
            if i == 'rain':
                return 'rain'
            if i == 'snow':
                return 'snow'
            break
        if i == 'fog':
            res = i
            break
        if i == 'clouds':
            res = i
            break
        if i == 'clear':
            res = i
            break
    return res


def check_forecast_for_warning(lat, lon):
    api_key = '1181b2bbbb3112b4983c8b37d478123e'
    url_forecast = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid=' + api_key
    response = requests.get(url_forecast).json()

    warnings_mas = []
    for i in range(len(response)):
        warnings_mas.append(check_includes_warning(response['list'][i]['weather'][0]['description']))

    if len(warnings_mas) > 0:
        return warning_priority(warnings_mas)
    if len(warnings_mas) == 0:
        return "clear"


def check_includes_warning(desc):
    if "clear" in str(desc):
        return 'clear'
    if "clouds" in str(desc):
        return 'clouds'
    if "snow" in str(desc):
        return 'snow'
    if "rain" in str(desc):
        return 'rain'
    if "thunderstorm" in str(desc):
        return 'thunderstorm'
    if "squalls" in str(desc):
        return 'squalls'
    if "tornado" in str(desc):
        return 'tornado'
    if str(desc) == "mist" or str(desc) == "smoke" or str(desc) == "haze" or str(desc) == "fog":
        return 'fog'
    if str(desc) == "sand" or str(desc) == "dust" or str(desc) == "ash":
        return 'dust'


def get_city_on_coord(lat, lon):
    geolocator = Nominatim(user_agent='test/1')
    location = geolocator.reverse(f'{lat},{lon}', language='en')
    loc_dict = location.raw

    if 'city' in loc_dict['address'].keys():
        return loc_dict['address']['city']
    else:
        return loc_dict['address']['municipality']


def get_current_weather_data_on_city(lat, lon):
    api_key = '1181b2bbbb3112b4983c8b37d478123e'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid=' + api_key

    city = str(get_city_on_coord(lat, lon))
    exist = False
    clear_old_weather_on_data()
    clear_old_weather_on_time()

    filtered_data = Weather_data.objects.filter(city_name=city)
    if city in Weather_data.objects.values_list('city_name', flat=True):
        exist = True

    if not exist:
        response = requests.get(url).json()

        # ______________

        weather_data = {'city_name': city,
                        'main': response['weather'][0]['main'],
                        'description': response['weather'][0]['description'],
                        'temp': int(response['main']['temp']),
                        'temp_min': int(response['main']['temp_min']),
                        'temp_max': int(response['main']['temp_max']),
                        'feels_like': int(response['main']['feels_like']),
                        'pressure': response['main']['pressure'],
                        'humidity': response['main']['humidity'],
                        'wind_speed': response['wind']['speed'],
                        'warning': check_forecast_for_warning(lat, lon),
                        'date': date.today(),
                        'time': datetime.datetime.now().time()
                        }

        new_obj_weath = Weather_data(city_name=weather_data['city_name'], main=weather_data['main'],
                                     description=weather_data['description'], temp=weather_data['temp'],
                                     temp_min=weather_data['temp_min'],
                                     temp_max=weather_data['temp_max'], feels_like=weather_data['feels_like'],
                                     pressure=weather_data['pressure'],
                                     humidity=weather_data['humidity'], wind_speed=weather_data['wind_speed'],
                                     warning=weather_data['warning'], date=date.today(),
                                     time=datetime.datetime.now().time())
        new_obj_weath.save()
        return weather_data

    if exist:
        serializer = WeatherDataSerializer(filtered_data[0])

        return serializer.data


def get_weatherforecast_data_on_city(lat, lon):
    api_key = '1181b2bbbb3112b4983c8b37d478123e'
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid=' + api_key

    response = requests.get(url).json()

    return response['list']


''' example-dict {'city_name': 'Moscow', 'temp': 3.19, 'temp_min': 2.78, 'temp_max': 4, 'feels_like': -3.59,
            'pressure': 1006, 'humidity': 56, 'wind_speed': 6}

    example-full-dict {'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 
    'main': {'temp': -11.27, 'feels_like': -17.55, 'temp_min': -12, 'temp_max': -11, 'pressure': 1016, 'humidity': 61}, 'visibility': 10000, 'wind': {'speed': 4, 'deg': 320}, 'clouds': {'all': 75}, 'dt': 1615301679,
    'sys': {'type': 1, 'id': 9027, 'country': 'RU', 'sunrise': 1615262432, 'sunset': 1615303191}, 'timezone': 10800, 'id': 524901, 'name': 'Moscow', 'cod': 200}
'''
