lista = []

item1 = input("Digite o primeiro item da lista de compras: ")
item2 = input("Digite o segundo item da lista de compras: ")
item3 = input("Digite o terceiro item da lista de compras: ")

lista.append(item1)
lista.append(item2)
lista.append(item3)

print("Lista:", lista)

remover = input("Qual item deseja remover? ")

try: 
    if remover in lista:
        lista.remove(remover)
        print("Item removido.")
except: 
    print("Item não encontrado.")

print("Lista atualizada:", lista)