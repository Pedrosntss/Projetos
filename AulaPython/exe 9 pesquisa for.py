procurar = input("Pesquisar peça: ")
estoque = ["Prego", "Porca", "Arruela", "Parafuso", "Mola"]
for item in estoque:
    if item == procurar:
        print("Item encontrado no estoque!")
        break #Interrompe o laço imediatamente
else:
    print("Item não encontrado após a varredura completa.")