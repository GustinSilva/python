"""
Crie um programa que leia nome de uma pessoa e mostre:
nome com todas as letras maiusculas
nome com todas as minusculas
quantas letras tem ao todo, sem considerar os espaços
quantas letas tem o primeiro nome
"""

nome = input('Digite o seu nome completo: ')
print('\033[7m', nome.upper(), '\033[m')

print('\033[4;42m', nome.lower(), '\033[m')

print(nome.capitalize())
print('\033[4;43m', nome.capitalize(), '\033[m')

print(nome.title())

a = nome.split()                        # separa nome em partes, depois une tudo sem espaços e da o comprimento
nomeJunto =''.join(a)
print(len(nomeJunto.strip()))

print(len(nome.split()[0]))             # comprimento do primeiro nome