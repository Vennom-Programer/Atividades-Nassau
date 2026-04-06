'''Escreva um algoritmo que solicite a idade de 10 pessoas e imprima: Total de pessoas com menos de 21 anos.
 Total de pessoas com mais de 50 anos.'''

menor_21 = 0
maior_50 = 0
for i in range(10):
    idade = int(input("Digite sua idade: "))

    if idade < 21:
        menor_21 += 1
    elif idade > 50: 
        maior_50 += 1
print("Total de pessoas com menos de 21 anos de idade é:", menor_21)
print("Total de pessoas com mais 50 anos de idade é:", maior_50)

print("Fim")
   