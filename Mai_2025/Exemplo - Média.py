nota1 = int(input("Digite a sua primeira nota: \n" ))
nota2 = int(input("Digite a sua segunda nota: \n" ))
nota3 = int(input("Digite a sua terceira nota: \n"))

notafinal = (nota1 + nota2 + nota3) / 3

if notafinal < 5:
    print("Você foi reprovado! sua média é de: ", notafinal)
elif notafinal <= 6.9:
    print ("Você ficou de recuperação! sua média é de: ", notafinal)
else:
    print("Você foi aprovado! sua média é de: ", notafinal)