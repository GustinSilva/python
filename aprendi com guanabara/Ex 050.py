"""
Faça um programa que leia 6, seis, numeros inteiros e mostre a soma apenas dos que forem pares
"""
soma = 0
for c in range(0, 6):
    num_dig = int(input('Digite um valor: '))
    if num_dig % 2 == 0:
        soma = soma + num_dig
print('A soma dos pares é de {}.'.format(soma))
