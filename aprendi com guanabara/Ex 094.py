"""
Crie um programa que leia nome sexo e idade de varias pessoas.... guarda os dados de cada um em um dicionario
e todos os dicionarios em uma lista
no final mostre
a - quantos foram cadastrados
b - a média de idade do grupo
c - uma lista com todas as mulheres
d - uma lista com as pessoas com idade acima da media
"""
grupo = list()
mulheres = list()
dados = dict()
somaId = medId = 0
while True:
    dados['nome'] = input('Nome: ').title()
    dados['sexo'] = input('Sexo: [M/F] ').upper()
    dados['idade'] = int(input('Idade: '))
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    cont = input('Quer continuar: [S/N] ').upper()
    grupo.append(dados.copy())
    somaId += dados['idade']
    if cont == 'N':
        break
medId = somaId / len(grupo)
print(f'Foram cadastradas {len(grupo)} pessoas.')
print(f'A média de idade é de {medId}')
print(mulheres)
for p in grupo:
    if p['idade'] >= medId:
        print()
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
