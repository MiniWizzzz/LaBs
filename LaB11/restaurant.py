# Класс ресторана
class Restaurant:

    def __init__(self, name: str, cuisin_type: str) -> None:
        self.name = name
        self.cuisin_type = cuisin_type

    def describe_restaurant(self):
        # Вывести название ресторана и тип кухни
        print(
            f"Название: {self.name} | Кухня: {self.cuisin_type}"
        )

    def open_restaurant(self):
        # Вывести состояние, открыт ли ресторан
        print("Ресторан открыт!")