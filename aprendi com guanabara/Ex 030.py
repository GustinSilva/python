"""
Crie um programa que leia um número inteiro e mostre se ele é par ou impar
"""

numero = int(input('Digite um número: '))
if numero % 2 == 1:
    print('\nO número é impar')
else:
    print('\nO número é par.')
print('O resto da divisão por 2 é {}.'.format(numero % 2))
