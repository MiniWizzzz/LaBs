import csv
import os
def LaB9():

    csv_path = os.path.join(os.getcwd(), "prise.csv")

    total = 0

    with open(csv_path, "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        next(reader)

        print("\nСписок покупок:")
        for item, count, price in reader:
            total += int(price) * int(count)
            print(f"{item}: {count} шт. за {price} руб.")
        print(f"\nИтоговая стоимость покупок: {total} руб.")

LaB9()