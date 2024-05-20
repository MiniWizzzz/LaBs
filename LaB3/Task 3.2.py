print("Вводите слова, используя Enter в конце каждого, и напишите stop, когда захотите остановиться")

word = ""
line = ""

while word != "stop":
    word = input()
    if word != "stop":
        line = line + word + " "

print("Ваша строка: ",line)