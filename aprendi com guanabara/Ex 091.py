"""
Crie um programa que onde 4 jogadores joguem um dado e tenham resultados aleatorios
guarde os resultados em um dicionario.
no final coloque o dicionario em ordem, sabendo que o vencedos tirou o maior numero do dado
"""
from random import randint
sorteado = {}
a = 1
for c in range(0, 4):
    dado = randint(1, 6)
    sorteado['jogador'+str(c+1)] = dado
print('Valores Sorteados: ')
for c, v in sorteado.items():
    print(f'O {c} tirou {v}.')
print('Ranking dos Jogadores: ')
for i in sorted(sorteado, key=sorteado.get, reverse=True):
    print(f'{a}ª Lugar: {i}, com {sorteado[i]}')
