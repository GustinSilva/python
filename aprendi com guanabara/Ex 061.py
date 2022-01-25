"""
Re569faça o desafio 51 onde leia o primeiro termo e a razão da PA, mostrando os 10 primeitos termos dela, usando o while
"""
print('Gerador de PA')
print('-=' * 15)
cont = 1
termo1 = float(input('Primeiro termo: '))
razao = float(input('Razão da PA: '))
while cont <= 11:
    print(f'{termo1:.0f} -> ' if cont <= 10 else 'FIM', end='')
    termo1 += razao
    cont += 1
