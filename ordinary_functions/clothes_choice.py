from ordinary_functions.get_weather_data import get_current_weather_data_on_city as get_weather

from ordinary_functions.get_weather_data import get_city_on_coord
from ordinary_functions.matrix import creating_clothes_matrix, creating_weather_matrix

import numpy as np
import datetime
from datetime import date

from personal_api.models import User_preferences


def algorithm(lat, lon, user_id):
    """
    Сопостовление обработанных данных с сервиса OpenWeatherMap с матрицей погоды и дальнейшее подстановка в матрицу одежды

    :param lat: широта
    :param lon: долгота
    :param user_id: уникальный токен пользователя
    :return: список предложенной одежды
    """
    m_weather = creating_weather_matrix()
    m_clothes = creating_clothes_matrix()

    real_weather = get_weather(lat, lon)
    wind_check = real_weather['wind_speed']
    humidity_check = real_weather['humidity']
    temp_check = real_weather['temp']
    f_coord = int(0)
    s_coord = int(0)
    th_coord = int(0)

    for i in range(len(m_weather) - 1):
        if m_weather[i][0][0] <= wind_check < m_weather[i + 1][0][0]:
            f_coord = i
            break

    for i in range(len(m_weather[0]) - 1):
        if m_weather[0][i][0] <= humidity_check < m_weather[0][i + 1][0]:
            s_coord = i
            break

    for i in range(len(m_weather[0][0])):
        if temp_check >= m_weather[0][0][i]:
            th_coord = i

    templ = User_preferences.objects.get(user_id=user_id)

    if templ.last_temp >= 20 or templ.last_temp <= -15:
        if templ.temp_pref != -100:
            th_coord += templ.temp_pref
            print("tempreture")

    if templ.last_temp == -100 and templ.last_hum == -100:
        th_coord += templ.temp_pref

    if 20 > templ.last_temp > -20:
        if templ.temp_pref != -100:
            s_coord += templ.temp_pref
            print("humidity")

    if th_coord >= 10:
        th_coord = 9

    if s_coord >= 6:
        s_coord = 5

    res = m_clothes[f_coord][s_coord][th_coord]

    if real_weather['warning'] == "rain":
        res.append('Umbrella')

    return res
