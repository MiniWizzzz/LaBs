import json
import os
from typing import Optional
from dataclasses import dataclass, asdict

JSON_PATH = os.path.join(os.getcwd(), "LaB10", "10_1.json")

@dataclass
class Product:
    name: str
    price: int
    weight: int
    available: Optional[bool]

def print_info(product: Product):
    print("Название:", product.name)
    print("Цена:", product.price)
    print("Вес:", product.weight)
    print("В наличии" if product.available else "Нет в наличии!")
    print(" ") # чисто для отступа



# ДОПОЛНЕНИЕ ДЛЯ ЗАДАЧИ 10.2
def new_product(data):
    new_info = input("Введите информацию через запятую: название,цена,вес:\n")
    try:
        name2, price2, weight2 = new_info.split(",")
        new_item = Product(
            name=name2,
            price=int(price2),
            weight=int(weight2),
            available=True,
        )
        data["products"].append(asdict(new_item))

        with open(JSON_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("Возможно, вы ошиблись при вводе.\nНет, вы абсолютно точно ошиблись.")



# дополненная условием задачка 10.1 (ура)
def Task_10_1():

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            products: list[dict] = data["products"]
            for p in products:
                product = Product(**p)
                print_info(product)

        dop_info = input("Добавить новые товары? [да/нет]: ") # не навязчиво интересуемся
        if dop_info == "да":
            new_product(data)

    except OSError:
        print("Проблемные проблемочки с файлом JSON")