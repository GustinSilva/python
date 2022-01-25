"""
Faça um programa que leia um número e mostre o seu fatorial
"""
from math import factorial
numero = int(input('Digite um valor para obter o fatorial: '))
cont = numero
print(f'Calculando {cont}! = ', end='')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print(factorial(numero))

cont2 = numero
print(f'Calculando {cont2}! = ', end='')
for c in range(numero, 0, -1):
    print(cont2, end='')
    print(' x ' if cont2 > 1 else ' = ', end='')
    cont2 -= 1
print(factorial(numero))
