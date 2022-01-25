"""
Reçada o desafi 035 dos triangulos, e acrescente o recurso que conte se ele é do tipo
Equilatero, possui os 3 lados iguais
isosceles, dois lados iguais
escaleno, todos os lados diferentes
"""
lado1 = float(input('Diga o lado 1: '))
lado2 = float(input('Diga o lado 2: '))
lado3 = float(input('Diga o lado 3: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('As medidas abaixo PODEM FORMAR um triangulo ', end='')
    if lado1 != lado2 != lado3 != lado1:
        print('ESCALENO.')
    elif lado1 == lado2 == lado3:
        print('EQUILÁTERO.')
    else:
        print('ISÓSCELES.')
else:
    print('As dimensões indicadas não podem formar um triangulo.')

