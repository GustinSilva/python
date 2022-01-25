"""
Crie um progrmaa que faça o computador jogar Jokempo com vc
"""
from time import sleep
import random

jogadas = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
jogador = int(input("""Suas opções de jogadas:
[0] Pedra
[1] Papel
[2] Tesoura 
Qual sua jogada: """))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 20)
print('Computador escolheu {}.'.format(jogadas[computador]))
print('Humano escolheu {}.'.format(jogadas[jogador]))
print('-=' * 20)
if computador == 0:  # Computador escolheu Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('HUMANO VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:  # Computador escolheu Papel
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('HUMANO VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # Computador escolheu Tesoura
    if jogador == 0:
        print('HUMANO VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
