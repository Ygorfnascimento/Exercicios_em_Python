idade = int(input("Digite a sua idade: "))

plano = int(input("Você possui uma doença pré-existente? \n 0. Não \n 1. Sim \n"))

if idade < 18:
    if plano == 0:
        print("A sua mensalidade é de: R$ 100")
    elif plano == 1:
        print("A sua mensalidade é de: R$ 150")
elif 18 <= idade <= 59:  
    if plano == 0:
        print("A sua mensalidade é de: R$ 200")
    elif plano == 1:
        print("A sua mensalidade é de: R$ 250")
else:  
    if plano == 0:
        print("A sua mensalidade é de: R$ 300")
    elif plano == 1:
        print("A sua mensalidade é de: R$ 350")