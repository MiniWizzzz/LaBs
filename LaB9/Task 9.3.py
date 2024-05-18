import csv
import os
def lab_9_3():

    csv_path = os.path.join(os.getcwd(), "prise.csv")

    total_price = 0

    with open(csv_path, "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        next(reader)

        print("Нужно купить:")
        for item, count, price in reader:
            total_price += int(price) * int(count)
            print(f"{item}: {count} шт. за {price} руб.")
        print(f"Итого: {total_price} руб.")

lab_9_3()