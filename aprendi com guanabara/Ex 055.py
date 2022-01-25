"""
Faça um programa que leia o peso de 5 pessoas e diga o maior e o menor pesos lidos
"""

quantidade = int(input('Quantidade de pessoas: '))
maior = 0
menor = 100
for c in range(0, quantidade):
    peso = float(input('Diga o peso: '))
    if peso > maior:
        maior = peso
    elif peso < maior:
        menor = peso
print(f'Nesse universo de {quantidade} pessoas, o maior peso é de {maior}kg e o menor é de {menor}kg.')
