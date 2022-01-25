import random

aluno1 = input('Diga o nome do aluno 1: ')
aluno2 = input('Diga o nome do aluno 2: ')
aluno3 = input('Diga o nome do aluno 3: ')
aluno4 = input('Diga o nome do aluno 4: ')

#lista é sempre entre colchetes []
lista = [aluno1, aluno2, aluno3, aluno4]

#escolha aleatória
print('\n\nO aluno escolhido foi: ', random.choice(lista))

#ordena os elementos
print(sorted(lista))
