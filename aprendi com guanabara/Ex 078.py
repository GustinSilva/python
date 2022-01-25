"""
Crie um programa que leia 5 valores e guarde em uma lista
no final mostre o maior, menor e sua posição
"""
lista = [int(input(f'Digite um valor: ')) for c in range(0, 5)]  # ou então pode ser lista = list()
print('-=' * 25)
print(f'Foram digitados os valores: ', lista)
print(f'\nO maior valor é {max(lista)} e está na posição ', end='')
for c, v in enumerate(lista):
    if v == max(lista):
        print(f'\033[35m{c}\033[m... ', end='')
print(f'\nO menor valor é {min(lista)} e está na posição ', end='')
for c, v in enumerate(lista):
    if v == min(lista):
        print(f'\033[36m{c}\033[m... ', end='')
