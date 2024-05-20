class RestaurantTwo:

    # задаю переменные
    def __init__(self, name: str, food_type: str, rate: float) -> None:
        self.name = name
        self.food_type = food_type
        self.rate = rate

    def describe_restaurant(self):
        # вывод названия ресторана и типа кухни
        print(
            f"Название: {self.name} | Кухня: {self.food_type} | Рейтинг: {self.rate}"
        )

    def update_rate(self, new_rate: float):
        # для установки рейтинга ресторана
        self.rate = new_rate
        print(f"Рейтинг {self.name} обновлен!")