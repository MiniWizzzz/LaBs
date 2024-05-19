from utils import get_weather
import tkinter as tk
from classes.weather_response import Location, Current

def info(weather: tuple[Location, Current]):

    # шаблон для оформления данных о погоде
    (location, current) = weather


    return (
        f"\nГород: {location.name} \n"
        f"Состояние погоды: {current.condition.text}\n"
        f"Температура: {int(current.temp_c)}°C (ощ-ся как {int(current.feelslike_c)}°C)\n"
        f"Видимость: {current.vis_km} км\n"
        )

def LaB13():

    # окно с компонентами

    window = tk.Tk()
    window.title("Погода")
    window.geometry("240x300")
    window.configure(padx=16, pady=8, bg="aliceblue")

    # надпись 1
    text = tk.Label(window, text="Введите город\n на английском", font=("Geometria Medium", 20),fg="dodgerblue", bg="aliceblue", pady=4)
    text.pack(fill="x")

    # надпись 2
    text2 = tk.Label(window, text="например, Saint Petersburg", font=("Geometria", 11), fg="dodgerblue",bg="aliceblue",pady=4)
    text2.pack(fill="x")

    # строка ввода названия города (по умолчанию Питер)
    entry = tk.Entry(window, font=("Geometria Medium", 12))
    entry.pack(fill="x", pady=6)

    # кнопка для вывода инфы, делаем по красоте
    button = tk.Button(
        window,
        text="Показать информацию",
        padx=12,
        pady=4,
        font=("Geometria Medium", 12),
        fg="white",
        bg="dodgerblue",
        command=lambda: info_label.configure(
            text=info(get_weather(entry.get())) # берем инфу из строки ввода и базы с weather api
        ),
    )
    button.pack(fill="x")

    info_label = tk.Label(window, text="", justify="left")
    info_label.pack(fill="x")

    window.mainloop()

LaB13()