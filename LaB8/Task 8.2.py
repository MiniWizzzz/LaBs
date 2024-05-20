from PIL import Image


a = {'Пасха': '1.jpg', 'пасха': '1.jpg', 'Рождество': '2.jpg', 'рождество': '2.jpg', '9 Мая': '3.jpg', '9 мая': '3.jpg'}
day = input("Открытку к какому празднику вывести: Пасха, Рождество, 9 Мая?\nПраздник: ")

img = Image.open(a[day])
#img = Image.open(elements'popug.jpg')
img.show()