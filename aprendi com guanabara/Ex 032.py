"""
Faça um programa que leia um ano e diga se ele é bissexto ou não
"""

ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é de fato um ano bissexto.'.format(ano))
else:
    print('O ano digitado, {}, não é um ano bissexto'.format(ano))
print(ano/4)
