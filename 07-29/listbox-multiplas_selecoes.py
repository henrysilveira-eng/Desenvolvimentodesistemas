import tkinter as tk

root = tk.Tk()
root.title("Listbox")

def selecao_mudou(eventos):
    sel = eventos.widget.curselection()
    itens = [eventos.widget.get(i) for i in sel]

    label.config(text=f"{', '.join(itens)} selecionado(s)!")

listbox = tk.Listbox(root, selectmode="multiple")
for item in ["Primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", selecao_mudou)

listbox.pack(expand=True)

label = tk.Label(root, text="Nenhum item selecionado")
label.pack()

root.mainloop()