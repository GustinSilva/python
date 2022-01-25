"""
Crie um programa que leia uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
no fim mostre a matriz na tela com a forma correta
"""
matriz = [[], [], []]
for c in range(0, 3):
    for d in range(0, 3):
        matriz[c].append(int(input('Diga um valor: ')))
for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{matriz[a][b]:^5}]', end='')
    print()
