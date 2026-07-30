linhas = [
"linha 1\n",
"linha 2\n",
"linha 3\n"
]

with open("08-07/escrita/saidas.txt", "w") as f:
         f.writelines(linhas)