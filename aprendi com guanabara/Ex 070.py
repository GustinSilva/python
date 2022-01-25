"""
Crie um programa que leia o nome e preço de vários produtos. o programa perguntará se usuário continuará
no final mostrar
qual o total gasto na compra
quantos produtos custam mais de 1000 reais
qual o nome do produto mais barato
"""
total = prodCaros = barato = cont = 0
print('-' * 50)
print('LOJA SUPER BARATÃO')
print('-' * 50)
while True:
    nome = input('Nome do Produto: ').strip()
    preco = int(input('Preço: R$ '))
    continuar = input('Quer continuar: [S/N] ').strip()[0]
    total += preco
    cont += 1
    if preco > 1000:
        prodCaros += 1
    if cont == 1:
        barato = preco
        nomeBarato = nome
    elif barato > preco:
        barato = preco
        nomeBarato = nome
    while not continuar in 'sSnN':
        continuar = input('Quer continuar: [S/N] ').strip()[0]
    if continuar in 'nN':
        break
print('-' * 50)
print(f'Foram comprados {cont} produtos, e o total foi de R$ {total:.2f}.')
print(f'Compramos {prodCaros} produtos que custaram mais de R$ 1,000.00.')
print(f'O produto mais barato foi {nomeBarato} com o preço de R$ {barato:.2f}.')
