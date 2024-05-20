class Restaurant:
    # Общий класс ресторана

    def __init__(self, name: str, cuisin_type: str, rate: float) -> None:
        self.name = name
        self.cuisin_type = cuisin_type
        self.rate = rate

    def describe_restaurant(self):
        print(
            f"Название: {self.name} | Кухня: {self.cuisin_type} | Рейтинг: {self.rate}"
        )

    def open_restaurant(self):
        print("Ресторан открыт!")

    def update_rate(self, new_rate: float):
        self.rate = new_rate
        print(f"Рейтинг {self.name} обновлен!")


# lab_12_1 lab 12_2
class IceCreamStand(Restaurant):

    def __init__(
        self,
        name: str,
        cuisin_type: str,
        rate: float,
        flavors: list[str],
    ) -> None:
        super().__init__(name, cuisin_type, rate)
        self.flavors = flavors

    def get_flavors(self):
        print("Вкусы мороженого:", ", ".join(self.flavors))
