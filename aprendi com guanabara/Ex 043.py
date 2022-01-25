"""
Desenvolva um programa que leia o peso e altura da pessoa e calculo o IMC
abaixo de 18,5 abaixo do peso
entre 18,5 e 25 peso ideal
entre 25 e 30 sobrepeso
entre 30 e 40 obesidade
acima de 40 obesidade morbida
"""
peso = float(input('Peso do paciente (kg): '))
altura = float(input('Altura do paciente (m): '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print('Está ABAIXO DO PESO.')
elif 18.5 < imc < 25:
    print('Está no PESO IDEAL.')
elif 25 < imc < 30:
    print('Está com SOBREPESO.')
elif 30 < imc < 40:
    print('Está com OBESIDADE.')
else:
    print('ESTÁ COM OBESIDADE MÓRBIDA.')
print('O seu IMC é de {:.2f}'.format(imc))
