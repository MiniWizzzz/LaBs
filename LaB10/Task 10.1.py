import json
import os
from typing import Optional
from dataclasses import dataclass, asdict

# прописываем путь к файлу сразу, чтобы не быть совсем дурачком
JSON_PATH = os.path.join(os.getcwd(), "LaB10", "10_1.json")

# прописываем типы данных для каждого вида информации
@dataclass
class Product:
    name: str
    price: int
    weight: int
    available: Optional[bool]

# оформляем вывод информации по-человечески
def print_info(product: Product):
    print("Название:", product.name)
    print("Цена:", product.price)
    print("Вес:", product.weight)
    print("В наличии" if product.available else "Нет в наличии!")
    print(" ") # чисто для отступа

# сама задачка 10.1 (ура)
def Task_10_1():
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            products: list[dict] = data["products"]
            for p in products:
                product = Product(**p)
                print_product_info(product)

    except OSError:
        print("Проблемные проблемочки с файлом JSON")