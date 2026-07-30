menu = [
    "Usuario",
    "etc",
    "sla"
]

largura = 30

print("+" + ("-" * largura) + "+")

for item in menu:
    print(f"|{item:^{largura}}|")
    
    print("+" + ("-" * largura) + "+")
