import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("300x280")

def calculador_IMC():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())

    imc = peso / (altura ** 2)

    if imc < 18.5:
        status = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        status = "Peso normal"
    elif 25 <= imc < 30:
        status = "Sobrepeso"
    else:
        status = "Obesidade"
    label_resultado.config(text=f"seu IMC é:{imc}, e vc está:{status}")

label_peso = tk.Label(root, text="Digite o seu Peso (kg):")
label_peso.pack(pady=5)

entry_peso = tk.Entry(root)
entry_peso.pack(pady=5)

label_altura = tk.Label(root, text="Digite a sua Altura (m):")
label_altura.pack(pady=5)

entry_altura = tk.Entry(root)
entry_altura.pack(pady=5)

botao_calcular = tk.Button(root, text="Calcular IMC", command=calculador_IMC)
botao_calcular.pack(pady=10)

label_resultado = tk.Label(root, text="Preencha os dados acima", font=("Arial", 10, "bold"))
label_resultado.pack(pady=10)

root.mainloop()

