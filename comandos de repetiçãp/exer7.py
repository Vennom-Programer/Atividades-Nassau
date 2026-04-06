total = 0
quantidade = 0
acima30 = 0
abaixo15 = 0

while True:
    temp = float(input("Digite a temperatura (999 para encerrar): "))

    if temp == 999:
        break

    total += temp
    quantidade += 1

    if temp > 30:
        acima30 += 1

    if temp < 15:
        abaixo15 += 1

if quantidade > 0:
    media = total / quantidade
else:
    media = 0

print("\nResultado:")
print("Quantidade de temperaturas:", quantidade)
print("Média das temperaturas:", media)
print("Acima de 30°C:", acima30)
print("Abaixo de 15°C:", abaixo15)