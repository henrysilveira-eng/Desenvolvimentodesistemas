import tkinter as tk
from tkinter import ttk

def realizar_conversao():
    try:
        valor = float(entry_valor.get())
        origem = combo_origem.get()
        destino = combo_destino.get()

        taxas = {
            "USD": 1.0,
            "BRL": 5.50,
            "EUR": 0.92,
            "GBP": 0.79,
            "JPY": 157.00
        }

        valor_em_dolar = valor / taxas[origem]
        valor_convertido = valor_em_dolar * taxas[destino]

        label_resultado.config(text=f"Resultado: {valor_convertido:.2f} {destino}")
    except ValueError:
        label_resultado.config(text="Erro: Insira um valor numérico válido.")

root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("300x250")

moedas = ["USD", "BRL", "EUR", "GBP", "JPY"]


ttk.Label(root, text="Val:").grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_valor = ttk.Entry(root)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="MO:").grid(row=1, column=0, padx=10, pady=10, sticky="E")
combo_origem = ttk.Combobox(root, values=moedas, state="readonly")
combo_origem.set("BRL")
combo_origem.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="MD:").grid(row=2, column=0, padx=10, pady=10, sticky="E")
combo_destino = ttk.Combobox(root, values=moedas, state="readonly")
combo_destino.set("USD")
combo_destino.grid(row=2, column=1, padx=10, pady=10)

btn_converter = ttk.Button(root, text="Converter", command=realizar_conversao)
btn_converter.grid(row=3, column=0, columnspan=2, pady=15)


label_resultado = ttk.Label(root, text="")
label_resultado.grid(row=4, column=0, columnspan=2)

root.mainloop()