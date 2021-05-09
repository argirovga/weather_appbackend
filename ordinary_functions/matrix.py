import numpy as np

'''
wind:
    1. 0-3 m/s  2. 3-6 m/s  3. 6-9 m/s  4. 9-12 m/s
    5. 12-15 m/s  6. 15-18 m/s  7. 18-21 m/s
    8. 21-24 m/s  9. 24-27 m/s  10. 27-30 m/s
'''
'''
humidity:
    1. 0-10%  2. 10-20%  3. 20-30%  4. 30-40%
    5. 40-50%  6. 50-60%  7. 60-70%
    8. 70-80%  9. 80-90%  10. 90-100%
'''
'''
temp:
    1. 0-4  2. 4-8  3. 8-12  4. 12-16  5. 16-20  6. 20-24
    7. 24-28  8. 28-32  9. 32-36  10. 36-40  11. 40-44
    12. 44-48  13. 48-52  14. 52-56  15. 56-60
'''


def temp_to_weather_matr(weather_matrix, temp, wind):
    start_temp = int(-20)
    for j in range(wind):
        for i in range(1, temp):
            weather_matrix[j][0][i] = start_temp
            start_temp += 5
        start_temp = -20

    return weather_matrix


def hum_to_weather_matr(weather_matrix, wind, hum):
    for j in range(wind):
        for i in range(1, hum):
            weather_matrix[j][i][0] = i * 20

    return weather_matrix


def wind_to_weather_matr(weather_matrix, wind):
    for i in range(1, wind):
        weather_matrix[i][0][0] = i * 5

    return weather_matrix


def creating_weather_matrix():
    weather_matrix = np.zeros(420, dtype=int)
    temp = int(10)
    hum = int(6)
    wind = int(7)
    weather_matrix = weather_matrix.reshape(wind, hum, temp)
    weather_matrix = temp_to_weather_matr(weather_matrix, temp, wind)
    weather_matrix = hum_to_weather_matr(weather_matrix, wind, hum)
    weather_matrix = wind_to_weather_matr(weather_matrix, wind)

    return weather_matrix


def creating_clothes_matrix():
    Ox = int(10)
    Oy = int(6)
    Oz = int(7)
    clothes_matrix = np.zeros(420, dtype=np.ndarray).reshape(Oz, Oy, Ox)
    clothes_matrix = adding_clothes_variants(clothes_matrix)

    return clothes_matrix


def adding_clothes_variants(clothes_matrix):
    # 0<=wind<5
    for i in range(0, 1):
        # temp>=20; 0<=hum<60; (["Sandals", "T-shirt", "Shorts", "Panama", "Sunglasses"])
        for j in range(0, 4):
            clothes_matrix[i][j][9] = ["Sandals", "T-shirt", "Shorts", "Panama", "Sunglasses"]
        # temp>=20; 60<=hum<=100; (["Sneakers", "T-shirt", "Shorts"])
        for j in range(4,6):
            clothes_matrix[i][j][9] = ["Sneakers", "T-shirt", "Shorts"]
        # 15<=temp<20; 0<=hum<=100; (["Sneakers", "T-shirt", "Hoodie", "Trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][8] = ["Sneakers", "T-shirt", "Hoodie", "Trousers"]
        # 10<=temp<15; 0<=hum<60; (["Sneakers", "T-shirt", "Coat", "Trousers"])
        for j in range(0,4):
            clothes_matrix[i][j][7] = ["Sneakers", "T-shirt", "Coat", "Trousers"]
        # 10<=temp<15; 60<=hum<=100; (["Sneakers", "T-shirt", "Waterproof coat", "Trousers"])
        for j in range(4, 6):
            clothes_matrix[i][j][7] = ["Sneakers", "T-shirt", "Waterproof coat", "Trousers"]
        # 5<=temp<10; 0<=hum<60; (["Demi boots", "Hoodie", "Coat", "Trousers"])
        for j in range(0, 4):
            clothes_matrix[i][j][6] = ["Demi boots", "Hoodie", "Coat", "Trousers"]
        # 5<=temp<10; 60<=hum<=100; (["Demi boots", "Hoodie", "Waterproof coat", "Trousers"])
        for j in range(4, 6):
            clothes_matrix[i][j][6] = ["Demi boots", "Hoodie", "Waterproof coat", "Trousers"]
        # 0<=temp<5; 0<=hum<=100; (["Demi boots", "T-shirt", "Coat", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][5] = ["Demi boots", "T-shirt", "Coat", "Warm trousers"]
        # -5<=temp<0; 0<=hum<=100; (["Winter boots", "T-shirt", "Winter coat", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][4] = ["Winter boots", "T-shirt", "Winter coat", "Warm trousers", "Warm hat"]
        # -10<=temp<-5; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][3] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat"]
        # -15<=temp<-10; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][2] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Gloves"]
        # -20<=temp<-15; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Scarf", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][1] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Scarf", "Gloves"]
        # temp<-20; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Thermal underwear", "Warm hat", "Scarf", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][0] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Thermal underwear", "Warm hat", "Scarf", "Gloves"]
    # 5<=wind<15
    for i in range(1, 3):
        # temp>=20; 0<=hum<60; (["Sandals", "T-shirt", "Shorts", "Panama", "Sunglasses"])
        for j in range(0, 4):
            clothes_matrix[i][j][9] = ["Sneakers", "T-shirt", "Shorts", "Panama"]
        # temp>=20; 60<=hum<=100; (["Sneakers", "T-shirt", "Shorts"])
        for j in range(4, 6):
            clothes_matrix[i][j][9] = ["Sneakers", "T-shirt", "Trousers"]
        # 15<=temp<20; 0<=hum<=100; (["Sneakers", "T-shirt", "Hoodie", "Trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][8] = ["Demi boots", "T-shirt", "Hoodie", "Trousers"]
        # 10<=temp<15; 0<=hum<60; (["Sneakers", "T-shirt", "Coat", "Trousers"])
        for j in range(0, 4):
            clothes_matrix[i][j][7] = ["Demi boots", "T-shirt", "Coat", "Trousers"]
        # 10<=temp<15; 60<=hum<=100; (["Sneakers", "T-shirt", "Waterproof coat", "Trousers"])
        for j in range(4, 6):
            clothes_matrix[i][j][7] = ["Demi boots", "T-shirt", "Waterproof coat", "Trousers"]
        # 5<=temp<10; 0<=hum<60; (["Demi boots", "Hoodie", "Coat", "Trousers"])
        for j in range(0, 4):
            clothes_matrix[i][j][6] = ["Demi boots", "Hoodie", "Coat", "Trousers"]
        # 5<=temp<10; 60<=hum<=100; (["Demi boots", "Hoodie", "Waterproof coat", "Trousers"])
        for j in range(4, 6):
            clothes_matrix[i][j][6] = ["Demi boots", "Hoodie", "Waterproof coat", "Trousers"]
        # 0<=temp<5; 0<=hum<=100; (["Demi boots", "T-shirt", "Coat", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][5] = ["Demi boots", "T-shirt", "Winter coat", "Warm trousers"]
        # -5<=temp<0; 0<=hum<=100; (["Winter boots", "T-shirt", "Winter coat", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][4] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat"]
        # -10<=temp<-5; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Scarf", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][3] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Scarf", "Warm hat"]
        # -15<=temp<-10; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][2] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Gloves"]
        # -20<=temp<-15; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Scarf", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][1] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Scarf", "Gloves"]
        # temp<-20; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Thermal underwear", "Warm hat", "Scarf", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][0] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Thermal underwear", "Warm hat", "Scarf", "Gloves"]
    # 15<=wind<=30
    for i in range(3, 7):
        # temp>=20; 0<=hum<60; (["Sandals", "T-shirt", "Shorts", "Panama"])
        for j in range(0, 4):
            clothes_matrix[i][j][9] = ["Demi boots", "T-shirt", "Hoodie", "Shorts", "Panama"]
        # temp>=20; 60<=hum<=100; (["Sneakers", "T-shirt", "Shorts"])
        for j in range(4, 6):
            clothes_matrix[i][j][9] = ["Demi boots", "T-shirt", "Trousers"]
        # 15<=temp<20; 0<=hum<=100; (["Sneakers", "T-shirt", "Hoodie", "Trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][8] = ["Demi boots", "T-shirt", "Hoodie", "Trousers"]
        # 10<=temp<15; 0<=hum<=100; (["Sneakers", "T-shirt", "Coat", "Trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][7] = ["Demi boots", "T-shirt", "Winter coat", "Trousers"]
        # 5<=temp<10; 0<=hum<60; (["Demi boots", "Hoodie", "Coat", "Trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][6] = ["Demi boots", "T-shirt", "Hoodie", "Winter Coat", "Trousers"]
        # 0<=temp<5; 0<=hum<=100; (["Demi boots", "T-shirt", "Coat", "Warm trousers", "Warm hat"s])
        for j in range(0, 6):
            clothes_matrix[i][j][5] = ["Demi boots", "T-shirt", "Winter coat", "Warm trousers", "Warm hat"]
        # -5<=temp<0; 0<=hum<=100; (["Winter boots", "T-shirt", "Winter coat", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][4] = ["Winter boots", "T-shirt", "Hoodie", "Winter coat", "Warm trousers", "Warm hat"]
        # -10<=temp<-5; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Scarf", "Warm trousers"])
        for j in range(0, 6):
            clothes_matrix[i][j][3] = ["Winter boots", "T-shirt", "Hoodie", "Winter coat", "Warm trousers", "Scarf", "Warm hat"]
        # -15<=temp<-10; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][2] = ["Winter boots", "T-shirt", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Gloves"]
        # -20<=temp<-15; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Scarf", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][1] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Warm hat", "Scarf",
                                       "Gloves"]
        # temp<-20; 0<=hum<=100; (["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Thermal underwear", "Warm hat", "Scarf", "Gloves"])
        for j in range(0, 6):
            clothes_matrix[i][j][0] = ["Winter boots", "Hoodie", "Winter coat", "Warm trousers", "Thermal underwear",
                                       "Warm hat", "Scarf", "Gloves"]

    return clothes_matrix


if __name__ == '__main__':
    print(creating_clothes_matrix())

