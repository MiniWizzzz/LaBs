days = ("понедельник","вторник","среда","четверг","пятница","суббота","воскресенье",)

num = input("Сколько выходных на неделе хочешь?: ")

try:
    if 0<int(num)<8:
        weekends = days[-int(num) :]        # берем дни с конца
        lost_week_days = days[: -int(num)]  # берем с начала
        print("Выходные дни: ", ", ".join(weekends))
        print("Рабочие дни: ", ", ".join(lost_week_days))
except ValueError:
    print("Значение введено неверно. Попробуй еще раз.")
except IndexError:
    print("Значение должно быть от 0 до 7")