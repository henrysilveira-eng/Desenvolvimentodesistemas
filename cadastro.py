import tkinter as tk
from tkinter import ttk  # O Combobox fica aqui dentro

    # Se quiser usar diretamente sem o prefixo .ttk
from tkinter.ttk import Combobox

def iniciar_app():
    root = tk.Tk()
    root.title("Formulário de Cadastro")
    root.geometry("700x300")

 # Configuração do Grid (ajusta o peso das colunas para melhor organização)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

        # --- Elementos de Layout ---
        # Imagem de perfil na Coluna 0 com rowspan de 5
        # Nota: Substitua 'perfil.png' pelo caminho da sua imagem.
    try:
            photo = tk.PhotoImage(file="Profile.png").subsample(3,3)
            img_label = tk.Label(root, image=photo)
            img_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)
    except:
            # Caso a imagem não exista, cria um espaço vazio ou um label de aviso
            img_label = tk.Label(root, text="[Imagem\nPerfil]", bg="gray", width=15, height=15)
            img_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

        # Definição dos campos (Label, Widget, Tipo/Opções)
    campos = [
        ("Nome:", tk.Entry(), "entrada"),
        ("Gênero:", ttk.Combobox(root, values=["Masculino", "Feminino"]), "combo"),
        ("Cor dos Olhos:", tk.Entry(), "entrada"),
        ("Altura (cm):", tk.Entry(), "entrada"),
        ("Peso (kg):", tk.Entry(), "entrada")
    ]

        # Criar os campos dinamicamente nas colunas 1 e 2
    for i, (texto, widget, tipo) in enumerate(campos):
        lbl = tk.Label(root, text=texto)
        lbl.grid(row=i, column=1, sticky="w", padx=5, pady=5)

        widget.grid(row=i, column=2, sticky="ew", padx=5, pady=5)

            # Se for combobox, ajustar a largura para preencher o espaço
        if tipo == "combo":
                widget.config(width=15)

        # Botão Enviar na última linha (Row 5), alinhado à direita
        # O span de colunas garante que ele possa ocupar o espaço visual das colunas 1 e 2
    btn_enviar = tk.Button(root, text="Enviar", command=lambda: print("Formulário enviado!"))
    btn_enviar.grid(row=5, column=1, columnspan=2, sticky="e", padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    iniciar_app()