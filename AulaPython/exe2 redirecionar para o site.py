import webbrowser
nome = input("Informe seu nome: ")
idade = int(input("informe sua idade: "))
if idade >= 13: 
    webbrowser.open("https://www.roblox.com")
else:
    print("="*20 + "JOGO +13" + "="*20)
    print(f"{nome}, você ainda é menor de idade.\nEsse site é destinado apenas para maiores de 13 anos")
