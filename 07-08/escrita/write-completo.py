n = [
"Ana",
"Bruno",
"Carlos"
]
with open("08-07/escrita/saidas.txt", "w") as f:
         for n in n:
             f.write(n + "\n")