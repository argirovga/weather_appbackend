from ordinary_functions.get_weather_data import get_current_weather_data_on_city as get_weather

from personal_api.models import Clothes_recommendation
from personal_api.serializers import ClothesRecommendationSerializer

import datetime
from datetime import date


def st_algorithm(city):
    weather = get_weather(city)
    dictionary_data = {}
    if weather['temp'] >= 23:
        dictionary_data = {'main_description': '1-layer clothing ',
                           'need_umbrella': False,
                           'type_of_hat': 'cap',
                           }
    if 23 > weather['temp'] >= 18:
        dictionary_data = {'main_description': '2-layer clothing ',
                           'need_umbrella': False,
                           'type_of_hat': None,
                           }
    if 18 > weather['temp'] >= 14:
        dictionary_data = {'main_description': '3-layer clothing ',
                           'need_umbrella': False,
                           'type_of_hat': 'warm hat',
                           }
    if 14 > weather['temp'] >= -2:
        dictionary_data = {'main_description': '4-layer clothing ',
                           'need_umbrella': False,
                           'type_of_hat': 'warm hat',
                           }
    if -2 > weather['temp'] >= -8:
        dictionary_data = {'main_description': '4-layer clothing ',
                           'need_umbrella': False,
                           'type_of_hat': 'extra-warm hat',
                           }
    if -8 > weather['temp'] >= -15:
        dictionary_data = {'main_description': '5-layer clothing ',
                           'need_umbrella': False,
                           'type_of_hat': 'extra-warm hat',
                           }

    if weather['humidity'] >= 70 or weather['temp'] >= 30:
        dictionary_data['need_umbrella'] = True

    dictionary_data['city_name'] = weather['city_name']
    dictionary_data['date'] = date.today()

    return dictionary_data


def bolvanka():
    dict = {'mas_clothes' : ['Boots', 'Trousers', 'T-shirt', 'Coat']}
    return dict


def clear_old_clothes_data():
    for i in Clothes_recommendation.objects.values_list('date', flat=True):
        if str(i) != str(date.today()):
            Clothes_recommendation.objects.filter(date=i).delete()


def weather_choice_mech(city):
    exist = False
    clear_old_clothes_data()

    filtered_data = Clothes_recommendation.objects.filter(city_name=city)
    if city in Clothes_recommendation.objects.values_list('city_name', flat=True):
        exist = True

    if exist:
        serializer = ClothesRecommendationSerializer(filtered_data[0])
        return serializer.data

    if not exist:
        response = st_algorithm(city)

        new_obj_weath = Clothes_recommendation(city_name=response['city_name'],
                                               main_description=response['main_description'],
                                               need_umbrella=response['need_umbrella'],
                                               type_of_hat=response['type_of_hat'],
                                               date=date.today())
        new_obj_weath.save()
        return response

    # return res
