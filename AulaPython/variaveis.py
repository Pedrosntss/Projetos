i= 0
qntd_refri = 0
total_refri = 0
qntd_burger = 0
total_burger = 0
print ("="*20 + "Lanchonete Senai" + "="*20)
nome_usuario = input("Digite seu nome: ")
print(f"Olá {nome_usuario}, Seja Benviado a lanchonete Senai!!")
print("-"*45)

print("="*10 + f" Cardapio Lanchonete " + "="*10)
print("\n1.Hamburguer Clássico - R$ 9.00")
print("\n2.Refrigerante - R$ 6.50\n")
print("="*45)
valor_burguer = float(9.0)
valor_refri = float(6.50)
qntd_pedido = int(input("Quantos lanches Deseja pedir?\n"))
for i in range(qntd_pedido):
    pedido = float(input("Informe seu pedido: "))
    if (pedido==1):
         qntd_burger = int(input("Quanto hamburgueres você deseja?\n"))
         total_burger = (qntd_burger*9)
    if(pedido==2): 
          qntd_refri = int(input("Quanto refrigerantes você deseja?\n"))
          total_refri = qntd_refri*6.50
print("="*20 + "TOTAL A PAGAR" + "="*20)
print(f"Hamburgueres: {qntd_burger} \nRefrigerante: {qntd_refri} ")
print(f"Total: R$ {total_burger+total_refri}")
print("="*53)
