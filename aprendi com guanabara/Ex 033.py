"""
Faça um programa que leia 3 números e fale qual é o maior e qual é o menor
"""
num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))
menor = num1

if num2 < num1 and num2 <num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
    
print('\nO menor número é {}. '. format(menor))
print('O maior número é {}. '.format(maior))

