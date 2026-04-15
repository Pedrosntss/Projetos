media = float(input("Digite media do aluno: "))
match media:
    case m if m >= 7.0 : 
         print(f"Aprovado! (Média: {media})")
    case m if m <= 5.0:
        print(f"Reprovado! (Média: {media})")
    case m if m >= 5.0:
        print(f"Em recuperação (Média: {media})") 
    case _:
        print("Média inválida! Digite novamente")