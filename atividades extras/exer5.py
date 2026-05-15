usuario_correto = "admin"
senha_correta = "1234"

tentativas = 0

while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso permitido")
        break

    else:
        print("Dados incorretos")
        tentativas += 1

if tentativas == 3:
    print("Acesso bloqueado")