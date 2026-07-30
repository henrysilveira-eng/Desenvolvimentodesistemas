def menu():
    print("\n0. Adicionar Filme (OPCIONAL)")
    print("1. Listar Filmes")
    print("2. Informações de um filme pelo titulo")
    print("3. Filmes de um Diretor específico")
    print("4. Filmes de um Gênero específico")
    print("5. Media de duração dos filmes")
    print("6. Sair")

def adicionar_filme():
    titulo = input("Digite o título do filme: ")
    ano = input("Insira o ano do filme: ")
    diretor = input("Insira o diretor do filme: ")
    genero = input("Insira o gênero do filme: ")
    duracao = input("Insira a duração em minutos (ex: 120): ")
    
    with open("0708/filmes.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\nTitulo: {titulo}\n")
        f.write(f"Ano: {ano}\n")
        f.write(f"Diretor: {diretor}\n")
        f.write(f"Genero: {genero}\n")
        f.write(f"Duracao: {duracao} minutos\n")
    print("Filme cadastrado com sucesso!")

def contador_filme():
    palavra_chave = "Titulo:"
    
    try:   
        with open("filmes/estrutura-filmes.txt", encoding="utf-8") as r:
            conteudo = r.read()
        if palavra_chave in conteudo:
            texto_apos = conteudo.partition(palavra_chave)[2]
            print(f"Titulo:\n{texto_apos.strip()}")
        else:
            print("A palavra-chave não foi encontrada no arquivo.")
            
    except FileNotFoundError:
        print("Erro: O arquivo 'estrutura-filmes.txt' não foi encontrado.")

def informacoes_filmes():
    palavra_chave = "Ano:"
    
    try:   
        with open("filmes/estrutura-filmes.txt", encoding="utf-8") as r:
            conteudo = r.read()
        if palavra_chave in conteudo:
            texto_apos = conteudo.partition(palavra_chave)[2]
            print(f"Titulo:\n{texto_apos.strip()}")
        else:
            print("A palavra-chave não foi encontrada no arquivo.")
            
    except FileNotFoundError:
        print("Erro: O arquivo 'estrutura-filmes.txt' não foi encontrado.")

def filmes_por_diretor():
    try:
        with open("0708/filmes.txt", encoding="utf-8") as f:
            diretor_buscado = input("digite o nome do diretor ao qual deseja saber os filmes: ").strip().lower()
            for linha in f:
                s = linha.strip().lower()
                if s.startswith("titulo:"):
                    ultimo_titulo = s.split(":", 1)[1].strip()
                elif s.strip().startswith("Diretor:"):
                    diretor = s.strip().split(":", 1)[1].strip()
                    if diretor == diretor_buscado:  
                        contador += 1
                        print(f"- {ultimo_titulo}")
    except FileNotFoundError:
        print("arquivo não encontrado.")
        return
    
    print(f"quantidade de filmes do diretor {diretor_buscado}: {contador}")
    return contador

def filmes_por_genero():
        print(" ")

def media_duração():
        print(" ")

while True: 
         
    menu()

    escolha = input("qual opção deseja escolher: ").strip()

    if escolha == "0":
        adicionar_filme()

    elif escolha == "1":
        contador_filmes()

    elif escolha == "2":
        inforacoes_titulo()

    elif escolha == "3":
        filmes_por_diretor()

    elif escolha == "4":
        filmes_por_genero()

    elif escolha == "5":
        media_duração()

    elif escolha == "6":
        print("encerrando sistema")
        break 

    else:
        print("opção invalida, digite novamente.")
