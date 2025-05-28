temperatura = 15
if temperatura > 25:
    print("Dia quente!")
elif temperatura > 15:
    print("Dia agrádavel!")
else:
    print("Dia frio!")

idade = int(input("Digite a sua idade: "))
if idade < 13:
    categoria = "Criança"
elif idade < 18:
    categoria = "Adolescente"
elif idade < 60:
    categoria = "adulto"
else:
    categoria = "idoso"

print(f"Você é classificado como: {categoria}")