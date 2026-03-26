# Entrada de dados
kg_morango = float(input("Digite a quantidade de morangos (kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (kg): "))

# Definindo preços
if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

# Calculando valores
total_morango = kg_morango * preco_morango
total_maca = kg_maca * preco_maca

total = total_morango + total_maca
peso_total = kg_morango + kg_maca

# Aplicando desconto
if peso_total > 8 or total > 25:
    desconto = total * 0.10
    total -= desconto

# Saída
print(f"Valor dos morangos: R$ {total_morango:.2f}")
print(f"Valor das maçãs: R$ {total_maca:.2f}")
print(f"Peso total: {peso_total:.2f} kg")
print(f"Valor final a pagar: R$ {total:.2f}")