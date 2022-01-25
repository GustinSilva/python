"""
Crie um programa que pergunte a distancia da viagem e calcule o preço da passagem
até 200 km , valor é de R$ 0,50/km
acima disso é R$ 0,45 por km
"""

distancia = float(input('Qual a distancia da sua viagem: '))
if distancia > 200:
    print('Como sua viagem é mais longa, o valor da passagem é de R$ {:.1f}0'.format(distancia*0.45))
else:
    print('A sua viagem é mais curta, o valor da passagem será de R$ {:.1f}0'.format(distancia*0.5))
