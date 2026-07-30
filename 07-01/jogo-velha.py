tabuleiro = [ [" ", " ", " "],
              [" ", " ", " "], 
              [" ", " ", " "]]

def exibir_tabuleiro():
    for i in range(len(tabuleiro)):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("-----------")


jogador = "X"

for jogada in range(9):
    exibir_tabuleiro()

    print(f"\nTurno do jogador: {jogador}")

    linha = int(input("Digite a linha do tabuleiro você deseja marcar: "))
    coluna = int(input("Digite a coluna do tabuleiro você deseja marcar: "))

    if tabuleiro[linha][coluna] != " ":
         print("Essa posição já está ocupada. Tente novamente.")
         continue

    tabuleiro[linha][coluna] = jogador

    venceu = False
    for i in range(3):
        if (
            tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " "
        ):  
            venceu = True
        if (
            tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " "
        ):  
            venceu = True
    if (
        tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " "
        or tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " "
    ):  
        venceu = True

    if venceu:
        exibir_tabuleiro()
        print(f"\njogador '{jogador}' win")
        break

    jogador = "O" if jogador == "X" else "X"
else:
    exibir_tabuleiro()
    print("\nbruh")