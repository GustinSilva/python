"""
Crie um programa que leia vários números inteiros pelo teclado. no final mostra a média entre todos e qual o maior e menor
o programa deve perguntar se o usuário quer continuar ou não
"""
resposta = ''
soma = 0
cont = 0
while resposta != 'N':
    valor = float(input('Digite um número: '))
    resposta = input('Ques continuar: S/N ').strip().upper()
    soma += valor
    cont += 1
    if cont == 1:
        maior = valor
        menor = valor
    elif maior < valor:
        maior = valor
    elif menor > valor:
        menor = valor
print(f'Você digitou {cont} valores, a soma é {soma}, a média foi {soma/cont}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
