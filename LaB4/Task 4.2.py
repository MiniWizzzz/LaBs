import re
def division():

    try:
        n = int(input("Введите число: "))
        print(f"100 / {n} = {100/n}")
    except ValueError:
        print("Ошибка: введите число!")
    except ZeroDivisionError:
        if n == 0:
            print("Ошибка: деление на ноль!")

division()
