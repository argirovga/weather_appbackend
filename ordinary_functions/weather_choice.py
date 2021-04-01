
def weather_choice_mech(weather):
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

    return dictionary_data