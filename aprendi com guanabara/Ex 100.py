"""
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteio e somapar
a primeira vai sortear 5 números e colocar eles dentro de uma lista e a segunda vai mostrar a soma entre os valores
pares sorteados pela função anterior
"""
from random import randint
from time import sleep
def sorteio(num):
    print('Sorteando 5 valores: ', end='')
    for c in range(0, 5):
        a = randint(0, 50)
        num.append(a)
        print(f'{a}..', end='')
        sleep(0.35)
    print('PRONTO!')

def somapar(lst):
    par = 0
    for d in lst:
        if d % 2 == 0:
            par += d
    print(f'Somando os valores pares de {lst}, temos {par}.')

# Programa principal
while True:
    numeros = []
    sorteio(numeros)
    somapar(numeros)
    cont = input('Continuar [S/N] ').strip().upper()
    if cont == 'N':
        break
print('FINALIZANDO ... ')