import tkinter as tk
from tkinter import messagebox


class RemoveItemButton(tk.Button):

    def __init__(self, parent: tk.Frame, listbox: tk.Listbox):
        super().__init__(parent,
            font=("Consolas", 8),
            text="Убрать",
            bg="lightcoral",
            borderwidth=0,
            command=self.remove_item,
        )
        self.listbox = listbox

    def remove_item(self):
        values = self.listbox.curselection()

        try:
            self.listbox.delete(values[0])
        except IndexError:
            messagebox.showwarning("Ой-ой...", "Чтобы удалить вкус, нужно его выбрать")
