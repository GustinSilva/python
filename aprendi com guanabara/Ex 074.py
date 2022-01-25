"""
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. depois mostre a listagem dos numeros gerados
e indique o maior e o menor
"""
from random import randint, sample
numeros = (randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor foi: {max(numeros)}')  # função max .. retorna maior valor da lista
print(f'O menor valor foi: {min(numeros)}')  # função min .... retorna menor valor da lista


a = tuple(sample(range(100), 15))  # sample .. seleciona valores aleatorios e depois so dizer quantas repetições da selação... problema numero nao repete
print(f'\n\nTupla com sample {a}')
print(f'Maior valor foi {max(a)} e o menor {min(a)}.')

b = list(sample(range(500), 15))
print(f'\n\nListagem com Sample {b}')
print(f'Maior valor foi {max(b)} e o menor {min(b)}.')
