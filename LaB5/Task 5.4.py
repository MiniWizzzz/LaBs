import random

a = ["Веселов", "Зайцев","Смирнов","Попов","Морозов","Кузнецов","Волков","Соколов","Игнатов","Петров"]
b = ["Бойко", "Иванов","Пахонин","Войтов","Дроздов","Анисимов","Самонин","Смородин","Балабан","Марков"]

c = []
n = 0
k = 0

print("\nИсходные списки групп:");
print(a)
print(b)

# добавляем в список команды по 5 случайных человек из каждой группы
while n < 5:
    c.append(a[random.randint(0, 9)])
    c.append(b[random.randint(0, 9)])
    n += 1

print("\nСпортивная команда: ", c)
print("\nКоличество игроков: ", len(c))
print("\nИгроки по алфавиту: ", sorted(c))

for c in c:
    if c == "Иванов":
        k = k + 1
        print("\nИванов есть")
        break
    else:
        print("\nИванова нет")
        break

print(k)