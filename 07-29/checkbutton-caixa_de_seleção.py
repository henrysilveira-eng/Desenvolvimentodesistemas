import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
checkbox_estado = tk.IntVar()

def mostrar_estado():
    if checkbox_estado.get():
        txt = "checked"
    else:
        txt = "unchecked"
    checkbox.config(
        text=f"check me! ({txt})"
    )

checkbox = tk.Checkbutton(root,
    text=f"check me! (checked)",
    variable=checkbox_estado,
    command=mostrar_estado)          

checkbox.select()
checkbox.pack(expand=True)

root.mainloop()