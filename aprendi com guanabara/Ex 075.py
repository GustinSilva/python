"""
Desenvolva um programa que leia quatro valores pelo teclado e mores
quantas vezes apareceu o numero 9
em que posição foi digitado o primeiro valor 3
quais foram os números pares
"""
numero = tuple(int(input(f'Diga o {c+1}º valor: ')) for c in range(0, 5))
print(f'O valor 9 apareceu {numero.count(9)} vezes')
print(f'O número 3 foi digitado na {numero.index(3)+1} posição' if 3 in numero else 'Não recebi o número 3.')
print('Os valores pares digitados foram: ', end='')
print({n for n in numero if n % 2 == 0}, end='')


