l = int(input("Digite o tamanho da linha que vc deseja:"))
c = int(input("Digite a quantidade de colunas que você deseja:"))

print("+" + ("-" * (l)) + "+")

for x in range(c):
    print("|" + (" " * l) + "|")

print("+" + ("-" * l) + "+")

print ("Retãngulo pronto")