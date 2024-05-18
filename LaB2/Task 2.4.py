print("Выберите 2 цвета из представленных: красный, синий, желтый")
colour_1 = str(input("Первый цвет: "))
colour_2 = str(input("Второй цвет: "))

a = str("красный")
b = str("синий")
c = str("желтый")

if (colour_1 == a) and (colour_2 == b):
    print("Результат смешения: фиолетовый")
elif (colour_1 == a) and (colour_2 == c):
    print("Результат смешения: оранжевый")
elif (colour_1 == b) and (colour_2 == c):
    print("Результат смешения: зеленый")
else:
    print("Ошибка при вводе цветов")