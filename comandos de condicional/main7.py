produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade:  "))
unitario = float(input("Digite o valor unitário: "))
total =( quantidade * unitario )
if quantidade *unitario <= 5:
  desconto = total* 0.02 
elif quantidade * unitario <=10:
   desconto = total* 0.03
if  quantidade * unitario >10:
    desconto = total * 0.05
totalPagar= (total - desconto)
print("O produto: ", produto )
print("Valor unitario:", unitario)
print("Total: ", total)
print("Total a pagar (com desconto): ", totalPagar)