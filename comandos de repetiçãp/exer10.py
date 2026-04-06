estoque = int(input("Digite a quantidade inicial em estoque: "))

while True:
    venda = int(input("Digite a quantidade vendida (0 para encerrar): "))

    if venda == 0:
        break

    estoque -= venda

    print("Estoque atual:", estoque)

    if estoque <= 0:
        print("Estoque zerado! Programa encerrado.")
        break

    if estoque < 10:
        print("Estoque baixo! Repor imediatamente.")