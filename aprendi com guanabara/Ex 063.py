"""
Crie um programa que leia um número N inteiro e mostre na tela os N primeiros elementos de uma sequencia de Fibonacci
"""
print('SEQUENCIA DE FIBONACCI')
print('~' * 25)
termos = int(input('Quantos termos iremos apresentar: '))
cont = 1
termo1 = 0
termo2 = 1
termo3 = 1
soma = 0
print(0, ' -> ', end='')
while cont <= termos+1:
    print(termo3, '-> ' if cont <= termos else ' Fim.', end='')
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    cont += 1
    soma += termo3
print(f'\nA soma final dos \033[32m{termos}\033[m primeiros termos é \033[4;35m{soma}\033[m.')
