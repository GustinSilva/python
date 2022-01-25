"""
faça um programa que leia o ano de nascimento de sete pessoas e diga no final quantos são maiores de idade e quantos não
"""

import datetime
quantidade = int(input('Quantas datas de nascimento teremos: '))
maior = 0
menor = 0
ano = datetime.date.today().year
for c in range(1, quantidade + 1):
    ano_nasc = int(input('Ano de Nascimento: '))
    if ano - ano_nasc >= 21:
        maior += 1
    else:
        menor += 1
print(f'Tvemos nesse universo de {quantidade} pessoa(s), {maior} maior(es) de idade e {menor} menor(es).')
