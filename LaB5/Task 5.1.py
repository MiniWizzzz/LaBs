import random

print("Я загадал 5 чисел от 1 до 20. Попробуй угадать одно из них!")

your_number = input("Твой ответ: ")
my_numbers = [random.randint(1, 20) for _ in range(5)]

if 0 < int(your_number) < 21:

    print("Я загадал:", my_numbers)

    if your_number in my_numbers:
        print("Ты угадал!")
    else:
        print("Увы, такого числа нет в списке")

else:
    print("Я же сказал: число должно быть от 1 до 20!!!")