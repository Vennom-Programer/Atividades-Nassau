soma_notas = 0
quantidade_alunos = 0

aprovados = 0
recuperacao = 0
reprovados = 0

while True:
    nota = float(input("Digite a nota (-1 para encerrar): "))

    if nota == -1:
        break

    soma_notas += nota
    quantidade_alunos += 1

    if nota >= 7:
        print("Aprovado")
        aprovados += 1

    elif nota >= 5:
        print("Recuperação")
        recuperacao += 1

    else:
        print("Reprovado")
        reprovados += 1

if quantidade_alunos > 0:
    media = soma_notas / quantidade_alunos
else:
    media = 0

print("\n--- RESULTADO ---")
print(f"Média da turma: {media:.2f}")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")