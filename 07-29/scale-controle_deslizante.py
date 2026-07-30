import tkinter as tk

# Inicializa a janela principal
root = tk.Tk()
root.title("Exemplo Scale")
root.geometry("300x200")


def valor_mudou(evento):
    label.config(text=evento)


scale = tk.Scale(
    root,
    from_=0,
    to=10,
    orient="horizontal",
    command=valor_mudou
)
scale.pack()

label = tk.Label(root, text="0")
label.pack()

# Executa a aplicação
root.mainloop()