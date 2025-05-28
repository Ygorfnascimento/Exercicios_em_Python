lista = []
lista_concluida = []

tarefa1 = input("Digite a primeira tarefa da lista de tarefas: ")
tarefa2 = input("Digite a segunda tarefa da lista de tarefas: ")

lista.append(tarefa1)
lista.append(tarefa2)

print("Sua lista atual: ", lista)

remover = input("Qual tarefa deseja remover? ")

try:
    lista.remove(remover)
    lista_concluida.append(remover)
    print("A tarefa foi removida! \nLista de tarefas pendentes: \n", lista)
except ValueError:
    print("A tarefa não está na lista atual.")

print("Lista de tarefas concluídas: ", lista_concluida)