"""
Faça um programa que mostre na tela todos os números pares entre 1 e 50
"""
intervalo = int(input('Fim do intervalo: '))
for c in range(1, intervalo+1):
    if c % 2 == 0:
        print(c, end='  ')
