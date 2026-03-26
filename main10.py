# Código correto e senha correta
codigo_correto = 1234
senha_correta = 9999

# Entrada do código
codigo = int(input("Digite o código do usuário: "))

# Verificação do código
if codigo != codigo_correto:
    print("Usuário inválido!")
else:
    # Se o código estiver correto, pede a senha
    senha = int(input("Digite a senha: "))
    
    if senha != senha_correta:
        print("Senha incorreta")
    else:
        print("Acesso permitido")