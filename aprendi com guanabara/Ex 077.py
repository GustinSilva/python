"""
Crie um programa que tenha uma tupla com várias palavras, sem usar acentos
depois vc deve mostrar para cada palavra quais são as vogais
"""
quant = int(input('Quantas palavras estudaremos: '))
palavra = tuple(input('Digite uma palavra: ').upper().strip() for c in range(0, quant))
vogais = ('aeiou')
for p in palavra:
    print(f'\nA palavra {p} possui as vogais ', end='')
    for letra in p:
        if letra.lower() in vogais:
            print(letra.lower(), end='')
