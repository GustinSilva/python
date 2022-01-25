"""
Escreva um programa que leia a velocidade de um carro
se ele ultrapassar 80km/h mostre a mensagem dizendo que ele foi multado
a multa custa R$ 7,00 por cada km acima do limite
"""
speed = float(input('Qual a velocidade do carro: '))
if speed <= 80:
    print('Está dentro do limite!!!')
else:
    print('Você foi multado!!!')
    print('O valor da multa será de R$ {:.1f}0.'.format((speed-80)*7))
