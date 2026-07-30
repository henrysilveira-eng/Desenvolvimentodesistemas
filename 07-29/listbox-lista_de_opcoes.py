import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()

def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        idx = sel[0]
        label.config(
            text=f"{evento.widget.get(idx)} Selecionado!")

listabox = tk.Listbox(root)
for item in["Primeiro", "Segundo", "Terceito"]:
    listabox.insert(tk.END, item)
listabox.bind("<<ListboxSelect>>", selecao_mudou)
listabox.pack(expand=True)
label = tk.Label(root, text="Primeiro Selecionado")
label.pack()

root.mainloop()