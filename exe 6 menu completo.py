#Inicializamos a vária opção 
opcao = 0 

while opcao != 3:
    print("\n --- Menu do Sistema ---")
    print("\n1. Saudação")
    print("\n2. informações do sistema")
    print("\n3. Sair")  

    #Recebendo entrada do usuário 
    try: 
        opcao = int(input("\nEscolha uma opção:"))
    except ValueError: 
        print("Digite apenas números!")
        continue

    # Estruturas de Decisão 
    if opcao == 1:
        print("\nOlá! Seja Benviado. É um prazer ajudar você! ☺️ ")
    elif opcao == 2:
        print("\nSistema: Python 3.10")
        print("\nStatus: Operacional")
    elif opcao == 3: 
        print("Saindo.. Até logo!")
    else:
        print("\nOpção invalida! Tente novamente")