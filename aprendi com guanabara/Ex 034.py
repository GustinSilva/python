"""
Escreva um programa que pergunte o salário do funcionário e calcule o aumento
salarios menores que 1250,00 aumento é 10%
salarios inferiores ou iguais a 1250,00 aumento de 15%
"""

salario = float(input('Diga-me qual o valor de seu salário: '))
if salario > 1250:
    aumento = salario * 1.1
    print('Seu novo salário será de R$ {}{:.2f}{}.'.format('\033[40m', aumento, '\033[m'))
else:
    aumento = salario * 1.15
    print('Parabéns, seu novo salário será de R$ {}{:.2f}{}.'.format('\033[43m', aumento,'\033[m'))
