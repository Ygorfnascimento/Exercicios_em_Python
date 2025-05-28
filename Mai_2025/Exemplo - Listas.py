produtos = ["tv", "celular", "notebook"]
vendas = [1500, 2000, 3000]

print("Os produtos são: ", produtos)
item_usuario = input("Qual item deseja remover: ")

try:
    produtos.remove(item_usuario)
    print("O produto '{}' foi excluído com sucesso".format(item_usuario))
    print("Produtos restantes: ", produtos)
except:
    print("O produto '{}' não existe na lista".format(item_usuario))

# i = produtos.index("celular")
# print("O valor de i é:", i)
# print("O produto da posição i é:", produtos[i])

# produto = input("Digite o nome de um produto (em letras minúsculas): ").lower()

#if produto in produtos:
   # i = produtos.index(produto)  
  #  qts_vendas = vendas[i]       
   # print("Foram realizadas {} vendas de {}".format(qts_vendas, produto))
#else:
   # print("O produto '{}' não existe nas vendas.".format(produto)) 

# produtos.append("monitor")
# print(produtos)

# produtos.remove("monitor")
# print(produtos)

# auxiliar = produtos.pop(1)
# print(auxiliar)
# print(produtos)