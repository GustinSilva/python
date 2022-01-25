"""
Faça um programa que leia o sexo de uma pessoa e só aceite valores 'F' ou 'M',
caso esteja errado peça a digitação novamente
"""
sexo = 'A'
while sexo not in 'masculino feminino':
    homem_mulher = input('Qual sexo da pessoa [M/F]: ')
    if homem_mulher in 'Mm':
        sexo = 'masculino'
    elif homem_mulher in 'fF':
        sexo = 'feminino'
    else:
        print('Essa letra não se refere a um sexo válido, gentileza ajustar.\n ')
print(f'\nObrigado por definir corretamente, sendo a pessoa do sexo {sexo.upper()}.')
