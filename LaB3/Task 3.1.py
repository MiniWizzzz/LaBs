N = int(input("Введите предполагаемое количество слов: "))

a = 1
line = ""
print("Введите указанное количество слов,используя Enter")
while a <= N:
    word = input()
    a += 1
    line = line + word + " "
print("Ваша строка: ",line)