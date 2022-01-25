"""
Crie um programa que simule um caixa eletronico. no inicio pergunte ao usuário qual sera o valor sacado
o programa informa quantas celulas de cada valor serao entregues
considere que o caixa possui cegulas de 50,20,10 e 1
"""
print('-' * 50)
print(f'{"BANCO AFS":^50}')
print('=' * 50)
valor = input('Qual valor deseja sacar: R$ ')
while not valor.isnumeric():
    valor = input('Qual valor deseja sacar: R$ ')
print('-' * 50)
resto = int(valor)
while True:
    if resto >= 50:
        quantidade = resto // 50
        resto = resto % 50
        nota = 50
    elif 20 <= resto < 50:
        quantidade = resto // 20
        resto = resto % 20
        nota = 20
    elif 10 <= resto < 20:
        quantidade = resto // 10
        resto = resto % 10
        nota = 10
    elif 1 <= resto < 10:
        quantidade = resto // 1
        nota = 1
        resto = 0
    elif resto == 0:
        break
    if quantidade != 0:
        print(f'Total de {quantidade} cédulas de R$ {nota:.2f}')
print('=' * 50)
print('Volte sempre ao Banco AFS! Tenha um bom dia!')
