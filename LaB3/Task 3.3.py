word = input("Введите любое слово: ")

b=1

for a in str(word):
    if a == "ф":
        print("Ого! Это редкое слово!")
        break
    else:
        b += 1
        if b == len(word):
            print("Эх, это не очень редкое слово...")
