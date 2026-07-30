with open("08-07/modo-leitura/exemplo.txt", "r") as f:
    linha1 = f.readline()
    linha2 = f.readline()
    print(linha1.strip())
    print(linha2.strip())
