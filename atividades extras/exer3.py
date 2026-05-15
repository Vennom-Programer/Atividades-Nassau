estoque = int(input("Digite a quantidade inicial em estoque: "))

while True:
    retirada = int(input("Digite a quantidade retirada (0 para encerrar): "))

    if retirada == 0:
        break

    estoque -= retirada

    if estoque < 0:
        estoque = 0

    print(f"Estoque atual: {estoque}")

    if estoque < 10 and estoque > 0:
        print("Estoque baixo")

    if estoque == 0:
        print("Estoque esgotado")
        break

print(f"\nEstoque restante: {estoque}")