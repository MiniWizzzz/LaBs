import random
example = ""
a = 0
b = 0
x = 0
y = 0
sum = 0

while a != 3:
    x = random.randint(1,10)
    y = random.randint(1,10)
    sum = x+y
    example = int(input(x))
    if int(example) == sum:
        print("Правильно!")
        b += 1
    else:
        print("Ответ неверный :(")
        a += 1

print("Игра окончена! Правильных ответов: ", b)