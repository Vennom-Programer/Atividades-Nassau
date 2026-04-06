'''A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 
horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um 
algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do 
funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês 
possua 4 semanas exatas). '''


horas_trabalhadas_mes = float(input("Digite as horas trabalhadas no mês: "))
salario_hora = float(input("Digite o salário por hora: "))
limite_horas = 160
horas_extras = 0.0
salario_total = 0.0

if horas_trabalhadas_mes <= limite_horas:
    salario_total = horas_trabalhadas_mes *salario_hora
    print(salario_total)
    
else:
    horas_extras = horas_trabalhadas_mes - limite_horas
    valor_extra = salario_hora *1.5
    salario_normal = limite_horas *salario_hora
    salario_extra = horas_extras * valor_extra
    salario_total = salario_normal + salario_extra
    print(salario_total)
    