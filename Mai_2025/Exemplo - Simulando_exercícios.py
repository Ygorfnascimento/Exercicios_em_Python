num = "10"
print(num)

num_int = int(num)
print(num_int)

nome = input("Digite o seu nome: ")
print(nome)

faturamento = True
print(type(faturamento))

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

print("Seu nome é " + nome + " e sua idade é " + idade)

var = "string"
print(var[0])  # Primeira letra da string

print(len(var))  # Comprimento da string

faturamento = 1000
custo = 500
print("O faturamento da loja foi de R$ {} e o custo foi de R$ {}".format(faturamento, custo))

print(type(faturamento))  # Tipo da variável faturamento

texto = "senai"
print(texto.capitalize())  # Primeira letra maiúscula

texto = "sENAI"
print(texto.casefold())  # Tudo minúsculo (mais forte que lower())

texto = "senai@gmail.com.br"
print(texto.count('.'))  # Conta quantos pontos (.) existem na string

texto = "senai@email.com.br"
print(texto.endswith("email.com.br"))  # Verifica se termina com determinado texto

texto = "senai@email.com.br"
print(texto.find("@"))  # Retorna o índice onde aparece o @

texto = "senai123"
print(texto.isalnum())  # Verifica se é alfanumérico (letras e números)
