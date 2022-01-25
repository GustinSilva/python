"""
crie um programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada o programa pergunte se o usuario
quer continuar
ao final mostre
quantos maiores de 18 anos
quantos homens cadastrados
mulheres menores de 20 anos
"""
maior18 = homem = mulheres20 = 0
while True:
    print('-' * 50)
    print('VAMOS CADASTRAR AS PESSOAS')
    print('-=' * 25)
    idade = int(input('Idade da pessoa: '))
    sexo = input('Sexo da pessoa [M/F]: ').strip()[0]
    while not sexo in 'MmFf':
        sexo = input('Sexo da Pessoa [M/F]: ').strip()[0]
    if idade > 18:
        maior18 += 1
    if sexo in 'mM':
        homem += 1
    elif sexo in 'fF' and idade > 20:
        mulheres20 += 1
    print('-' * 50)
    continuar = input('Quer continuar? [S/N]: ').strip()[0]
    while not continuar in 'SsNn':
        continuar = input('Quer Continuar? [S/N]: ').strip()[0]
    if continuar in 'nN':
        break
print(f'FIM DO PROGRAMA')
print(f'Temos {maior18} pessoas maiore de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Tivemos {mulheres20} mulheres com mais de 20 anos.')


