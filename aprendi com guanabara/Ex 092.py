"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho... cadastre com idade...em um dicionario
se for acaso CTPS diferente de zero o dicionario tambem recebera ano de contratação e o salario
calcule ea crescente alem da idade com quantos anos a pessoa vai aposentar
"""
from datetime import datetime
dados = dict()
dados['nome'] = input('Nome: ').strip().title()
dados['idade'] = datetime.today().year - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario: '] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['contratacao'] - datetime.today().year + 35
print(dados)
for c, v in dados.items():
    print(f'{c} tem o valor {v}')
