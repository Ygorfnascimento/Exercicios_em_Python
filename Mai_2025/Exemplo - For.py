alunos = []
notas = []

for i in range(3):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    
    alunos.append(nome)
    notas.append(nota)

print("\nLista de alunos e suas notas:")
for i in range(3):
    print(f"{alunos[i]}: {notas[i]}")

produtos = ["coca", "pepsi", "guaraná"]
producao = [15000, 12000, 14000]

tamanho = len(produtos)

for i in range(tamanho):
    print(f"A produção de {produtos[i]} é de: {producao[i]}")

for produto in produtos:
    i = produtos.index(produto)
    print(f"Produção de {produto} e o index é: {i}")

vendas = [50, 100, 200, 300, 400, 500]
meta = 300
qtd_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtd_bateu_meta += 1

qtd_funcionarios = len (vendas)
print("O percentul de funcionários, que bateram a meta foram de {:.1%}".format(qtd_bateu_meta / qtd_funcionarios))

funcionarios =["Maria", "João", "Pedro", "José"]

for i, funcionario in enumerate(funcionarios):
    print(f"O index {i} é o funcionário {funcionario}")

estoque = [300, 350, 200, 50, 450]
produtos = ["coca", "pepsi", "dolly", "café", "guaraná"]
nivel_minimo = 300

for i, qtd in enumerate(estoque):
    if qtd < nivel_minimo:
        print(f"O produto {produtos[i]} está com o nível baixo: {qtd} unidades.")

alunos = ["João", "Maria", "Gabryel" "José"]
valor_procurado = "José"

for aluno in alunos:
    if aluno == valor_procurado:
        print(f"Encontramos o aluno {aluno}.")
        continue
    else:
        print(f"Aluno: {aluno}.")

vendas = []

venda = input("Digite o nome do produto e tecle ENTER para registrar, para cancelar tecle ENTER sem digitar nada: ")

while venda != "":
    vendas.append(venda)
    venda = input("Digite o nome do produto e tecle ENTER para registrar, para cancelar tecle ENTER sem digitar nada: ")

print(f"Registros finalizados, as vendas foram: {vendas}")
