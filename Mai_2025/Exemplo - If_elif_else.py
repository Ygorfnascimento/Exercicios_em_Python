if "@" in "senai@email.com":
    print("Tem @")
else:
    print("Não tem @")

if not "#" in "senai@email.com":
    print("Não tem #")
else:
    print("Tem #")

idade = int(input("Digite a sua idade: "))
assinatura = False

if idade >= 18 and assinatura:
    print("Acesso ilimitado a todo conteúdo premium.")
elif idade >= 18:
    print("Acesso ilimitado, considere assinar o plano premium, para mais benefícios.")
else:
    print("Acesso restrito ao conteúdo + 18.")

idade = int(input("Digite a sua idade: "))
assinatura = int(input("Você tem a assinatura premium: \n 0. Não \n 1. Sim \n"))

if idade >= 18 and assinatura == 1:
    print("Acesso ilimitado a todo conteúdo premium.")
elif idade >= 18:
    print("Acesso ilimitado, considere assinar o plano premium, para mais benefícios.")
else:
    print("Acesso restrito ao conteúdo +18.")


