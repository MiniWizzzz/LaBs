
def division():

    try:
        n = int(input("Введите число: "))
        a = round(100/n, 2)
        print(f"100 / {n} = {a}")
    except ValueError:
        print("Ошибка: введите число!")
    except ZeroDivisionError:
        if n == 0:
            print("Ошибка: деление на ноль!")

division()
