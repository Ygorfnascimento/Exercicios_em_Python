lista_de_alunos = []
notas_dos_alunos = []

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")

lista_de_alunos.append(aluno1)
lista_de_alunos.append(aluno2)
lista_de_alunos.append(aluno3)

nota1 = int(input("Nota do aluno {}: ".format(aluno1)))
nota2 = int(input("Nota do aluno {}: ".format(aluno2)))
nota3 = int(input("Nota do aluno {}: ".format(aluno3)))

notas_dos_alunos.append(nota1)
notas_dos_alunos.append(nota2)
notas_dos_alunos.append(nota3)

print("\nLista de alunos:", lista_de_alunos)
print("Notas dos alunos:", notas_dos_alunos)

aluno = input("\nQual aluno você quer mudar a nota? ")

try:
    i = lista_de_alunos.index(aluno)
    nova_nota = int(input("Nova nota do  {}: ".format(aluno)))
    notas_dos_alunos[i] = nova_nota
except ValueError:
    print("O aluno não pode ser encontrado.")

print("\nNotas atualizadas:", notas_dos_alunos)