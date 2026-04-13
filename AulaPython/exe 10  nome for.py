for tentativa in range (1,4):
    nome = input(f"Digite seu nome (tentativa {tentativa}/3): ").strip()

    if nome != "":
        print (f"Olá, {nome}! Tudo bem?")
        break
    print("Você não digitou o nome!")

else:
    # Só roda se esgotou as 3 tentativas
    print ("Tentativa esgotadas.")
