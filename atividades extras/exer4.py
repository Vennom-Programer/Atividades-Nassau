soma_temperaturas = 0
quantidade_temperaturas = 0

frios = 0
agradaveis = 0
quentes = 0

while True:
    temperatura = float(input("Digite a temperatura (999 para encerrar): "))

    if temperatura == 999:
        break

    soma_temperaturas += temperatura
    quantidade_temperaturas += 1

    if temperatura < 15:
        print("Frio")
        frios += 1

    elif temperatura <= 30:
        print("Agradável")
        agradaveis += 1

    else:
        print("Quente")
        quentes += 1

if quantidade_temperaturas > 0:
    media = soma_temperaturas / quantidade_temperaturas
else:
    media = 0

print("\n--- RESULTADO ---")
print(f"Média das temperaturas: {media:.2f}°C")
print(f"Dias frios: {frios}")
print(f"Dias agradáveis: {agradaveis}")
print(f"Dias quentes: {quentes}")