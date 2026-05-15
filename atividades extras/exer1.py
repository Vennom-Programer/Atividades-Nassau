total_vendido = 0
quantidade_vendas = 0

vendas_baixas = 0
vendas_medias = 0
vendas_altas = 0

while True:
    venda = float(input("Digite o valor da venda (0 para encerrar): "))

    if venda == 0:
        break

    total_vendido += venda
    quantidade_vendas += 1

    if venda <= 100:
        print("Venda baixa")
        vendas_baixas += 1

    elif venda <= 500:
        print("Venda média")
        vendas_medias += 1

    else:
        print("Venda alta")
        vendas_altas += 1

print("\n--- RESULTADO ---")
print(f"Total vendido: R$ {total_vendido:.2f}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Vendas baixas: {vendas_baixas}")
print(f"Vendas médias: {vendas_medias}")
print(f"Vendas altas: {vendas_altas}")