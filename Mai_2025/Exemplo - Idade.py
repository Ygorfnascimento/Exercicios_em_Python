idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade <= 59:
    print("Você é adulto.")
else:
    print("Você é idoso.")