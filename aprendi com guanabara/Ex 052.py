"""
Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
"""
cont = int(0)
numero = int(input("Diga um número inteiro: "))
for c in range(1, numero+1):
    if numero % c == 0:
        cont += 1
if cont < 3:
    print(f'O número {numero} é PRIMO.')
else:
    print(f'O número {numero} não é um número PRIMO.')
