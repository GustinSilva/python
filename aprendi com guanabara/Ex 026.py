"""
Faça um programa que leia uma frase pelo teclado
quantas vezes aparece letra A
em que posição aparece primeiro
em que posição aparece pela última vez
"""

frase = input('Digite uma frase: ')
fraseLower = frase.lower()

print('A letra A aparece {} vez(es).'.format(fraseLower.count('a')))

print('A letra A inicia a aparição na posição {}.'.format(fraseLower.strip().find('a')+1)) # FIND da esquerda para direita

print('A letra A aparece a última vez na posição {}'.format(fraseLower.strip().rfind('a')+1))  # RFIND da direita para esquerda