import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()

def enter_pressionado(event):
    label.config(text=event.widget.grt())

entry = tk.Entry(root)
entry.insert(0, "Digite seu Texto:")
entry.bind("<Return>", enter_pressionado)
entry.pack()

label = tk.Label(root, text="Demonstração")
label.pack()

root.mainloop()