"""
crie um progrma que leia nome idade e sexo de 4 pessoas e mostre
media de idade do grupo
qual nome do mais velho
quantas mulheres tem menos de 20 anos
"""
soma_idade = 0
mulheres = 0
maior_idade = 0
nome_velho = ''
quantidade = int(input('Quantas pessoas cadastraremos: '))
for c in range(0, quantidade):
    nome = input("Nome: ").strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M / F]: ').strip()
    soma_idade += idade
    media_idade = soma_idade / quantidade
    if sexo in 'Mm' and idade > maior_idade:
        nome_velho = nome
        maior_idade = idade
    elif sexo in 'Ff' and idade < 20:
        mulheres += 1
print(f'A média de idade do grupo é de {media_idade:.2f} anos.')
print(f'O homem mais velho é o Sr. {nome_velho} com {maior_idade} anos.')
print(f'Temos {mulheres} mulheres com menos de 20 anos.')
