import random

aluno1 = input('Digite o aluno 1: ')
aluno2 = input('Digite o aluno 2: ')
aluno3 = input('Digite o aluno 3: ')
aluno4 = input('Digite o aluno 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

#shuffle é embaralhar, faz a mistura na lista apresentada
random.shuffle(lista)

print('\nA ordem de apresentação será \n\n{}'.format(lista))
