"""
Faça um programa que leia o nome completo de uma pessoa mostrando separadamente o primeito e último nome
"""

nome = input('Digite o nome completo:')

print('Primeiro nome: {}'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[-1]))
