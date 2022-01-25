"""
Crie um programa que leita nome de uma cidade e diga se ela começa com Santo
"""

cidade = input('Diga o nome da cidade: ')
cidadePartido = cidade.split()[0]

print(cidadePartido.lower() == 'santo')
print(cidadePartido)