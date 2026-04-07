usuario_correto = "instrutor"
senha_correta = "senai123"
print("=== 🔐 SISTEMA DE ACESSO SENAI ===")
usuario = input("Digite seu usuario: ")
while usuario != usuario_correto:
    usuario = input("Usuario incorreto, digite novamente: ")
senha = input("Digite sua senha: ")
while senha != senha_correta:
    senha = input("Senha incorreta, digite novamente: ")