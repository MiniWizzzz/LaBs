from classes.restaurant import IceCreamStand

def lab_12_1():

    ice1 = IceCreamStand(
        "BrandIce",
        "мороженое",
        4.32,
        ["ваниль", "фисташка", "шоколад"]
    )
    ice1.describe_restaurant()
    ice1.get_flavors()
    ice1.open_restaurant()
lab_12_1()



