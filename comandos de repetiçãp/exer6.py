total = 0
quantidade = 0

while True:
    valor = float(input("Digite o valor da venda (0 para encerrar): "))

    if valor == 0:
        break

    total += valor
    quantidade += 1

if quantidade > 0:
    media = total / quantidade
else:
    media = 0

print("\nResumo do dia:")
print("Total vendido: R$", total)
print("Quantidade de vendas:", quantidade)
print("Média das vendas: R$", media)