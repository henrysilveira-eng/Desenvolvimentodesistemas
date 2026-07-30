n = input("digite 3 nomes separados por ',': ").split(",")

with open("08-07/escrita/saidas.txt", "w") as f:
    for nome in n:
        f.write(nome + "\n")