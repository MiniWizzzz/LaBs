class Restaurant:

    def __init__(self, name: str, cuisin_type: str, rate: float) -> None:
        self.name = name
        self.cuisin_type = cuisin_type
        self.rate = rate

    def describe_restaurant(self):
        print(f"Название: {self.name} | Кухня: {self.cuisin_type} | Рейтинг: {self.rate}")

    def open_restaurant(self):
        print("Ресторан открыт!")

    def update_rate(self, new_rate: float):
        self.rate = new_rate
        print(f"Рейтинг {self.name} обновлен!")


# lab_12_1 lab 12_2
class IceCreamStand(Restaurant):
    # Все, что касается морожки

    def __init__(
        self,
        name: str,
        food_type: str,
        rate: float,
        flavors: list[str],
        location: str,
        work_start: int,
        work_end: int,
    ) -> None:
        super().__init__(name, food_type, rate)
        self.flavors = flavors
        self.location = location
        self.work_start_at = work_start
        self.work_end_at = work_end

    def get_flavors(self):
        print("Вкусы мороженого:", ", ".join(self.flavors))

    def is_exist_flavor(self, name):
        # Есть ли такой вкус
        return name in self.flavors

    def yes_or_no_flavor(self, fl: str):
        # для добавления вкуса
        if self.yes_or_no_flavor(fl):
            print("Вкус уже есть в асортименте")
        else:
            self.flavors.append(fl)
            print(f'Вкус "{fl}" добавлен в асортимент')

    def remove_flavor(self, fl: str):
        # для удаления вкуса (зо што)
        if self.yes_or_no_flavor(fl):
            self.flavors.remove(fl)
            print(f'Вкус "{fl}" убран из асортимента')
        else:
            print(f"Такой вкус не входит в асортимент магазина {self.name}.")
            print("В асортименте:", ", ".join(self.flavors))