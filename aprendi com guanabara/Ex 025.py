"""
Crie um programa que leia o nome de uma pessoa e diga se ele tem Silva no nome
"""

nome = input('Digite seu nome: ').lower().split()

print('Existe Silva em seu nome: {}'.format('silva' in nome))
