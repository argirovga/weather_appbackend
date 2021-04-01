import requests
from datetime import date


def get_current_weather_data_on_city(city: str):
    api_key = '1181b2bbbb3112b4983c8b37d478123e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

    response = requests.get(url.format(city)).json()

    dictionary_data = {'city_name': response['name'],
                       'temp': response['main']['temp'],
                       'temp_min': response['main']['temp_min'],
                       'temp_max': response['main']['temp_max'],
                       'feels_like': response['main']['feels_like'],
                       'pressure': response['main']['pressure'],
                       'humidity': response['main']['humidity'],
                       'wind_speed': response['wind']['speed'],
                       'date': str(date.today)
                       }
    return dictionary_data


def get_weatherforecast_data_on_city(city: str):
    api_key = '1181b2bbbb3112b4983c8b37d478123e'
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=' + api_key

    response = requests.get(url.format(city)).json()

    return response['list']


if __name__ == '__main__':
    print(get_weatherforecast_data_on_city('Moscow'))

''' example-dict {'city_name': 'Moscow', 'temp': 3.19, 'temp_min': 2.78, 'temp_max': 4, 'feels_like': -3.59,
            'pressure': 1006, 'humidity': 56, 'wind_speed': 6}

    example-full-dict {'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 
    'main': {'temp': -11.27, 'feels_like': -17.55, 'temp_min': -12, 'temp_max': -11, 'pressure': 1016, 'humidity': 61}, 'visibility': 10000, 'wind': {'speed': 4, 'deg': 320}, 'clouds': {'all': 75}, 'dt': 1615301679,
    'sys': {'type': 1, 'id': 9027, 'country': 'RU', 'sunrise': 1615262432, 'sunset': 1615303191}, 'timezone': 10800, 'id': 524901, 'name': 'Moscow', 'cod': 200}
'''
