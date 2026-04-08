#essas variaveis é informção pra o for rodar.
salario_total = 0
maior_idade = 0
menor_idade = 0
mulheres_acima_3mil = 0
qtd_acima_50 = 0

for i in range(20):
    print(f"\ncliente {i+1}")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo M/F): ")
    salario = float(input("Digite o salario: "))

    # Soma dos salario
    salario_total += salario

    # Maior idade
    if i ==0:
        maior_idade = idade
        menor_idade = idade
    else:
        if  idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade

    # Mulhres com salario acima de 3000
    if sexo =="F" and salario > 3000:
        mulheres_acima_3mil +=1

    # Pessoas com mais de 50 anos
    if idade > 50:
        qtd_acima_50 +=1

# Resultados

media = salario_total / 20
percentual_acima_de_50 = (qtd_acima_50 /20) * 100
print("\n Resultados")
print("Media Salarial", media )
print("Maior Idade", maior_idade )
print("Menor Idade", menor_idade )
print("Mulheres acima de 3mil", mulheres_acima_3mil )
print("Percentual de pessoas acima de 50 anos", qtd_acima_50,"%")