tabuleiro = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

def exibir_tabuleiro():
         for i in range(len(tabuleiro)):
                 print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
                 if i > 2:
                         print('------------------')
