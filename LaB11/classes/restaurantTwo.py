class RestaurantTwo:

    # Класс ресторана
    def __init__(self, name: str, cuisin_type: str, rate: float) -> None:
        self.name = name
        self.cuisin_type = cuisin_type
        self.rate = rate

    def describe_restaurant(self):
        # Вывести название ресторана и тип кухни
        print(
            f"Название: {self.name} | Кухня: {self.cuisin_type} | Рейтинг: {self.rate}"
        )

    def update_rate(self, new_rate: float):
        # Установить рейтинг заведения
        self.rate = new_rate
        print(f"Рейтинг {self.name} обновлен!")