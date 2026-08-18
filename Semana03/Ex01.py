horas = float(input("Digite o total de horas trabalhadas:"))
salario = horas * 35

if salario < 1000:
    salario = salario + 300
else:
    salario = salario

print("O salário final é R$:", salario)
