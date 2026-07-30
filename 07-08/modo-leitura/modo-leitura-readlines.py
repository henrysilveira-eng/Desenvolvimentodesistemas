with open("08-07/modo-leitura/exemplo.txt", "r") as f:
    linhas = f.readlines()
    for linha in linhas:
        print(linha.strip())