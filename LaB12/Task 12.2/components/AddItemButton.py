import tkinter as tk


class AddItemButton(tk.Button):

    def __init__(self, parent: tk.Frame, root: tk.Tk, add_to: tk.Listbox):
        super().__init__(parent,
            font=("Geometria Medium", 8),
            text="Добавить",
            bg="turquoise",
            borderwidth=0,
            command=self.open_modal,)

        self.root = root
        self.listbox = add_to

    def add_item_to_listbox(self, value: str):
        self.listbox.insert(self.listbox.size(), value)

    def open_modal(self):
        # модальное окно для добавления вкуса
        modal = tk.Toplevel(self.root, padx=8, pady=8, bg="MintCream")
        modal.title("Добавить вкус")
        modal.geometry("200x110")

        # стиль и расположение заголовка
        name_label = tk.Label(
            modal, text="Название вкуса", font=("Geometria Medium", 16, "bold"), fg="teal",bg="MintCream")
        name_label.pack(side="top", anchor="n")

        name_value = tk.Text(modal, height=1)
        name_value.pack(side="top", fill="x", anchor="n")

        btn_add = tk.Button(
            modal,
            text="Добавить!!!",
            font=("Geometria Medium", 10),
            bg="turquoise",
            command=lambda: self.add_item_to_listbox(
                value=name_value.get("1.0", "end")
            ),
        )
        btn_add.pack(side="top", fill="x", anchor="n") # центровка
