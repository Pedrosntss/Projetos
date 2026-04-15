while True:
    comando = input("Escreva a ação que dese realizar em seu jogo: ").lower()

    match comando:
        case "salvar": 
            print ("Salvando o seu jogo...")
        case "carregar": 
            print("carregando o jogo salvo...") 
        case "sair":
            print("Saindo do jogo...")
        case _:
            print ("Comando invalido! Tente novamente.")
    break