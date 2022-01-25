"""
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça ao usuário que tente descobrir
o número escolhido
O programa deverá escrever na tela se o usuário acertou ou nao
"""
import random

numero = random.randint(0, 5)
tentativa = int(input('Digite sua tentativa: '))
if numero == tentativa:
    print('Parabéns, vc acertou o número que pensei!!!')
else:
    print('Vc não acertou, tente novamente. \nPensei no número {}{}{}. '.format('\033[4;34m', numero, '\033[m'))
