import random
example = ""
a = 0   # это количество ошибок
b = 0   # это количество правильных ответов
x = 0   # первое слагаемое
y = 0   # второе слагаемое
sum = 0 # результат, с которым сравниваем овтет

while a != 3:
    x = random.randint(1,10)
    y = random.randint(1,10)
    sum = x+y
    example = int(input(f"{x} + {y} = "))

    if int(example) == sum:
        print("Правильно!")
        b += 1
    else:
        print("Ответ неверный :(")
        a += 1

print("Игра окончена! Правильных ответов: ", b)