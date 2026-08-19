num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

if num1 < num2:
    print("num1, num2")
else:
    print("num2, num1")

    # EX Número 1 ( ex número 2 Abaixo)

ano_nascimento = int(input("Digite o ano de nascimento:"))

idade = 2026 - ano_nascimento

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar infelizmente :)")
