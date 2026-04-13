usuarioC = "Pedro"
SenhaC = "2008"

for tentativa in range (1,4):
    Usuario = input(f"Digite seu nome (tentativa {tentativa}/3): ").strip()
    senha = input(f"Digite sua senha (tentativa {tentativa}/3): ").strip()

    if Usuario == usuarioC and senha == SenhaC:
        print (f"Olá, {usuarioC}! Seja bem vindo!!")
        break
    print("Usuario ou senha incorretos!!")

else:
    # Só roda se esgotou as 3 tentativas
    print ("Tentativa esgotadas.")
