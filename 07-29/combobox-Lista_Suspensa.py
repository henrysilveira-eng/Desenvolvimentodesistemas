import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
combobox = ttk.Combobox(root, values=["primeiro", "segundo", "terceiro"])

def selecao_mudou(evento):
    label.config(text = f"{evento.widget()} selecionado!")

combobox.set("primeiro")
combobox.bind("<<ComboboxSelected>>", selecao_mudou)

combobox.pack()
label = tk.Label(root, text="Primeiro Selecionado!")
label.pack()

root.mainloop()
