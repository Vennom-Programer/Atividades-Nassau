salario_fixo = float (input("Digite o salário fixo: "))
Vendas = float (input("Digite o valor das vendas:"))

if Vendas <= 1500:
    comissao = Vendas * 0.03
else:
    comissao = (1500 * 0.03) + ((Vendas - 1500) * 0.05)

salario_total = salario_fixo + comissao

print(f"Salário total: R$ {salario_total:.2f}")