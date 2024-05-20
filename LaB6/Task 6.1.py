dictionary = {'Россия': 'Москва', 'Япония': 'Токио', 'Китай': 'Пекин', 'Франция': 'Париж'}

print("Страны и их столицы: ", dictionary)

country = input(str("\nСтолицу какой страны хотите вывести?: "))
print("Столица этой страны -", dictionary[country])

print("\nА вот все страны по порядку:")
list_keys = list(dictionary.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', dictionary[i])