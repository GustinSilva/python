"""
Refaça o desafio 9, mostrando a tabuada de um número que o usuáiro escolher, so que agora usando o laço for
"""
numero = int(input('Qual tabuada deseja descobrir: '))
for c in range(0, 11):
    produto = numero * c
    print('{} x {} = {}'.format(numero, c, produto))
