import random
print( "=" * 45)
print(" "*13+"Quem Vai ao Quadro??")
print("=" * 45)

turma = [
    "Eduardo Sambay Cavalari",
    "Emily Pereira Doliveira",
    "Gabriel Santana Nadolny Pec",
    "João Pedro Albino Scotti",
    "Joaquim Bomfim Zacarias",
    "Matheus Alencar Do Nascimento",
    "Vinícius Carneiro Maciel",
    "Vitor Hugo Parnaiba Amorim",
    "Abiner Alves Paz",
    "Afonso Alves Takasugui Filho",
    "Alysson Del Rosal Pawlack",
    "Andrey Gonçalves Carneiro",
    "Antonio Gabriel Santos De Almeida",
    "Anuar Martins De Lima",
    "Carlos Eduardo Cidral De Siqueira",
    "Cauã Amaral Rocha",
    "Cauan Henrique Macedo Santos",
    "Daniel Dalla Rosa Dos Santos",
    "Eduardo Moreti Da Freiria",
    "Fabio Augusto Vaz",
    "Felipe Mello Pereira",
    "Felipe Reiz Navas",
    "Gabriel Junqueira Mamede",
    "Guilherme Mazzo Roberto",
    "Henrique Cochinski",
    "Henrique Portinho Nauiack",
    "Hilan Santos Teixeira De Paula",
    "Izadora Venâncio Prestes",
    "João Marcos Santos Rebá",
    "Leonardo Antonio Cruz",
    "Luis Eduardo De Aquino",
    "Marco Antonio De Souza Vitto",
    "Marcos Antonio Domingos Prina Junior",
    "Maria Clara Faustina Pereira",
    "Mateus André Staut",
    "Mateus Klinczak Belotti",
    "Pedro Henrique Silva Dos Santos",
    "Rodrigo Kamaroski Evangelista",
    "Vandré Luiz Barros Santana",
    "Wederson Ferreira Roberto"
]

random.shuffle(turma) #Shuffle embaralha tudo, todos os nomes
sorteado1 = random.choice(turma) #choice escolhe um aleatóriamente
turma.remove(sorteado1) #remove o sorteado da lista para não ser sorteado novamente
sorteado2= random.choice(turma)

print(f"1° sorteado: {sorteado1}")
print(f"2° sorteado: {sorteado2}")
print("\n" + "=" * 45)
