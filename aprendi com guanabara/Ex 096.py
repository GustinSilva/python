"""
Faça um programa que tenha uma função chamada area(), recebe as dimensoes do terreno retangular e mostra a área
"""
def area (a, b):
    s = a * b
    print(f'A área de um terreno de {a} x {b} é de {s}m².')

print('Controle de Terrenos')
print('-' * 25)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
