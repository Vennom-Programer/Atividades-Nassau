litrosvendido=int(input("qual a quantidade de litros vendidos: "))
combustivel = input("qual o combustivel: A OU G ")

if combustivel =="A":
    preco=2.90

if combustivel =="G":
    preco=3.30

if combustivel == "A":
    if litrosvendido <= 20:
        desconto = 0.03
    else:
        desconto = 0.05

if combustivel == "G":
    if litrosvendido <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
valor = litrosvendido * preco
valordesconto = valor * desconto
valorfinal = valor - valordesconto

print("O valor a pagar é:", valorfinal)