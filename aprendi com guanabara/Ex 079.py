"""
Crie um programa que o usuário digite vários valores numéricos e os cadastre em lista
caso o numero exista não será adicionado
no final exibir todos os valores unicos digitados em ordem crescente
"""
cont = int(input('Quantos valores serão lidos: '))
lista = []
c = 0
while c in range(0, cont):
    temp = int(input(f'Diga o {c+1}º valor: '))
    if temp in lista:
        print('Valor já incluso, gentileza digite outro.')
    else:
        lista.append(temp)
        c += 1
print(f'Foram digitados os valores, em ordem: {sorted(lista)}')
