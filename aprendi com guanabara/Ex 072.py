"""
Crie um programa que tenha uma contagem por extenso de zero ate vinte,
seu programa deverá ler um número pelo teclado entre 0 e 20, e mostrar ele por extenso
"""
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numeral = int(input('Digite um número entre 0 e 20: '))
while not 0 <= numeral <= 20:
    numeral = int(input('Valor não válido, digite novamente: '))
print(f'Você digitou o número {extenso[numeral]}.')
