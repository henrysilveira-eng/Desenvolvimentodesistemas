print("1 - fahrenheit para Celsius")
print("2 - celsius para Fahrenheit")
escolha = input("Escolha a opção 1 ou 2: ")

if escolha == "1":
    f_str = input("Digite quantos Fahrenheit estão agora: ")
    f = float(f_str.replace(',', '.'))
    c = (f - 32) * 5 / 9
    
    print(f"Agora estão {c:.1f}° Celsius.")

elif escolha == "2":
    c_str = input("Digite quantos Celsius estão agora: ")
    c = float(c_str.replace(',', '.'))
    f = (c * 9 / 5) + 32
    
    print(f"Agora estão {f:.1f}° Fahrenheit.")

else:
    print("Opção inválida! Por favor, rode o programa novamente e digite 1 ou 2.")