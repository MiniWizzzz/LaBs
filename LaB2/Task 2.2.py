
number = int(input("Введите номер посадочного места от 1 до 54: "))

if (number >= 1) and (number <= 36):
    a = "купе,"
elif (number >= 37) and (number <= 54):
    a = "плацкарта,"

if number % 2 == 0:
    b = "верхняя полка"
else:
    b = "нижняя полка"

if (number >= 1) and (number <= 54):
    print("Ваше место", number, ":", a, b)
else:
    print("Не верно введен номер посадочного места.\nПроверьте правильность ввода.")