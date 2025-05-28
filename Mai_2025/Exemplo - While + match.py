vendas = ("João", "01/01/2025", "25/03/2002", 2000, "Estagiário")
print(vendas)

vendas = ("Maria",)
print(vendas[0])

vendas = ("João", "01/01/2025", "25/03/2002", 2000, "Estagiário")
nome, data_admissao, data_nascimento, salario, cargo = vendas

print(nome)
print(data_admissao)
print(data_nascimento)
print(salario)
print(cargo)

while True:
    print("Isso vai executar pelo menos uma vez.")

    resposta = input("Deseja continuar? (s/n): ").lower()

    if resposta != "s":
        break

print(resposta)

while True:
    dia = int(input("Digite o número do dia da semana (1-7): "))

    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")
        case 7:
            print("Sábado")
        case _:
            print("Valor inválido!")