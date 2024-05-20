import tkinter as tk
from classes.restaurant import IceCreamStand

from components.AddItemButton import AddItemButton
from components.RemoveItemButton import RemoveItemButton

def lab_12_2():
    # данные о магазине
    ice1 = IceCreamStand(
        "BrandIce",
        "мороженое",
        4.32,
        ["ваниль", "фисташка", "шоколад"],
        "проспект Проспектов, дом не завезли",
        10,
        21,
    )

    app = tk.Tk()
    app.title("Карточка магазина")  # наименование для окна
    app.geometry("600x200")         # общий размер окна
    for c in range(3):              # колонки
        app.columnconfigure(index=c, weight=4)
        app.rowconfigure(index=c, weight=4)

    # фрейм для информации о магазине (слева)
    frame = tk.Frame(app, bg="MintCream")
    frame.pack(side="left", padx=4, pady=4, fill="both", expand=True)

    # стиль и расположение названия магазина
    text_brand = tk.Label(frame, text=ice1.name, font=("Geometria Medium", 40, "bold"),fg="teal",bg="MintCream")
    text_brand.pack(side="top", anchor="nw")
    # стиль и расположение рейтинга магазина
    text_rate = tk.Label(frame, text=f"Рейтинг: {ice1.rate}", font=("Geometria Medium", 16), bg="turquoise")
    text_rate.pack(side="top", anchor="nw")
    # стиль и расположение часов работы магазина
    text_time = tk.Label(frame,text=f"Время работы: {ice1.work_start_at}-{ice1.work_end_at}",font=("Geometria Medium", 12),fg="teal",bg="MintCream")
    text_time.pack(side="bottom", anchor="sw")
    # стиль и расположение местонахождения магазина
    text_location = tk.Label(frame,text=f"Место: {ice1.location}",font=("Geometria Medium", 12),fg="teal",bg="MintCream")
    text_location.pack(side="bottom", anchor="sw")

    # фрейм для информации о вкусах мороженого (справа)
    frame_flavors = tk.Frame(app, bg="MintCream")
    frame_flavors.pack(side="right", padx=4)

    # вывод списка со вкусами мороженого
    flavors_list = tk.Listbox(frame_flavors)
    for i, fl in enumerate(ice1.flavors):
        flavors_list.insert(i, fl)
    flavors_list.pack(side="top")

    # кнопки добавить/убрать
    btn_add = AddItemButton(parent=frame_flavors, root=app, add_to=flavors_list)
    btn_add.pack(side="left", fill="x", expand=True)
    btn_remove = RemoveItemButton(frame_flavors, flavors_list)
    btn_remove.pack(side="right", fill="x", expand=True)

    app.mainloop()

lab_12_2()