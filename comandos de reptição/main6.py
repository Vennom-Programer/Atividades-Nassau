nome = input("digite seu nome:")
sexo = input("digite seu sexo (m ou f):")
altura = float(input("digite sua altura:"))

if sexo == "m":
    peso_ideal = (72.7 * altura) - 58
    print(f"{nome} seu peso ideal é {peso_ideal:.2f} kg:")
elif sexo == "f":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"{nome} seu peso ideal é {peso_ideal:.2f} kg:")