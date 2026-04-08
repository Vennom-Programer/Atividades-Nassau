votosA = 0
votosB = 0
votosC = 0

while True:
    voto = int(input("Vote: 1-Cand.A | 2-Cand.B | 3-Cand.C | 0-Encerrar:"))

    if voto == 0:
        break
    elif voto == 1:
        votosA +=1
    elif voto == 2:
        votosB +=1
    elif voto == 3:
        votosC +=1
    else:
        print("Voto inválido")

total = votosA + votosB + votosC

print(f"Candidato A: {votosA} votos")
print(f"candidato B: {votosB} votos")
print(f"candidato C: {votosC} votos")
print(f"Total válidos: {total}")

if votosA > votosB and votosA > votosC:
    print("Vencedor: Candidato A!")
elif votosB > votosA and votosB > votosC:
    print("Vencedor: Candidato B!")
elif votosC > votosA and votosC > votosB:
    print("Vencedor: Candidato C!")
else:
    print("Houve empate!")