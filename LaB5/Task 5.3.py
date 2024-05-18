days = ("понедельник","вторник","среда","четверг","пятница","суббота","воскресенье",)

num = input("Сколько выходных на неделе хотите: ")

try:
    if 0<int(num)<8:
        weekends = days[-int(num) :]
        lost_week_days = days[: -int(num)]
        print("Ваши выходные дни: ", ", ".join(weekends))
        print("Ваши рабочие дни: ", ", ".join(lost_week_days))
except ValueError:
    print("Значение введено неверно. Попробуй еще раз")
except IndexError:
    print("Значение должно быть от 0 до 7")