"""
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta
no final mostre um boletim com a média de cada um e permita que o usuário mostre as notas de cada aluno individualmente
"""
lista = list()
while True:
    nome = str(input('Diga o nome: ')).strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    cont = str(input('Quer continuar: [S/N]')).upper()
    if cont in 'nN':
        break
print('-=' * 25)
print(f'{"No.":<4}{"NOME":<9}{"MÉDIA":>5}')
print('-' * 50)
for c, a in enumerate(lista):
    print(f'{c:<4}{a[0]:<9}{a[2]:>5}')
print('-' * 50)
while True:
    vernota = int(input('Mostrar notas de qual aluno (999 sair): '))
    if vernota == 999:
        break
    elif 0 <= vernota <= len(lista):
        print(f'Notas de {lista[vernota][0]} são {lista[vernota][1]}')
    else:
        print('Fora da lista.')
    print('-' * 50)
print('FINALIZANDO ...')
print('<<< VOLTE SEMPRE >>>')
