import random
from classes.restaurantTwo import RestaurantTwo

def lab_11_2():
    # Создание нескольких экземпляров ресторана
    restaurantOne = RestaurantTwo("Чебуречкино", "фастфуд", 4.35)
    restaurantTwo = RestaurantTwo("Мясо и хлеб", "грузинская", 5.0)
    restaurantThree = RestaurantTwo("Плов готов", "армянская", 4.25)

    restaurantOne.describe_restaurant()
    restaurantTwo.describe_restaurant()
    restaurantThree.describe_restaurant()

    # lab_11_3
    restaurantOne.update_rate(new_rate = round(random.uniform(1, 5),2))
    restaurantOne.describe_restaurant()
lab_11_2()