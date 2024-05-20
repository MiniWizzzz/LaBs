# Класс ресторана
class Restaurant:

    # задаю переменные
    def __init__(self, name: str, food_type: str) -> None:
        self.name = name
        self.food_type = food_type

    def describe_restaurant(self):
        # вывод названия ресторана и типа кухни
        print(
            f"Название: {self.name} | Кухня: {self.food_type}"
        )

    def open_restaurant(self):
        # тут вывожу, что ресторан открыт
        print("Ресторан открыт!")