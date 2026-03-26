saldo = float(input("Digite o saldo da sua conta: "))
debito = float(input("Digite o debito da sua conta: "))
credito = float(input("Digite o credito da sua conta: "))

if  (saldo - debito + credito) < 0:
    print("Saldo negativo")
else:
    print("saldo positivo")