"""
Escreva um programa que leia dois números inteiros, compare e escreva
o primeiro é maior
o segundo é maior ou
os dois são iguais
"""
print('-=' * 20)
print('   BEM VINDO AO SUPER NUMBER ANALISIS')
print('-=' * 20)

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if num1 > num2:
    print('O primeiro valor digitado {}{}{} é o \033[36m{}\033[m.'.format('\033[4;32m', num1, '\033[m', 'Maior'))
elif num2 > num1:
    print('O segundo valor digitado {}{}{} é o \033[7;36m{}\033[m.'.format('\033[4;32m', num2, '\033[m', 'Maior'))
else:
    print('Os números digitados são iguais!!!')
