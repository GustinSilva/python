"""
Faça um programa que ajude um jogador da mega sena.
o programa vai perguntar quantos jogos serão gerados e sorteie 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo
em uma lista composta
"""
from random import randint
jogos = []
aposta = int(input('Quantos jogos teremos: '))
for a in range(0, aposta):
    cont = 0
    while cont < 6:
        numero = randint(0, 60)
        if numero not in jogos:
            jogos.append(numero)
            cont += 1
    jogos.sort()
    print(f'{jogos}')
    jogos.clear()
