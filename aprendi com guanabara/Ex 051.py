"""
Crie um programa que leia o primeiro termo e a razao de uma PA
mostre os 10 primeiros termos da progressão
"""
prim_termo = int(input('Primeiro termo da progressão: '))
razao = int(input("Razão da PA: "))
for c in range(0, 11):
    print(prim_termo, end='  ')
    prim_termo += razao
