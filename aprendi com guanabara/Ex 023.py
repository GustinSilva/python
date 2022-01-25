import random

numero = random.randint(0, 9999)
numero1 = str(10000+numero)

print('Numero gerado foi: ', numero)
print('\033[4;34munidade:', numero1[4])
print('dezena: ', numero1[3])
print('centena:', numero1[2])
print('milhar: ', numero1[1], '\033[m')

print('\nOutra forma: \n')

unid = numero // 1 % 10         # Divisão inteira por 1 e o resto dessa divisão por 10
dez = numero // 10 % 10
cent = numero // 100 % 10
mil = numero // 1000 % 10
print('Unidade: {}{}{}'.format('\033[4;36m', unid, '\033[m'))
print('Dezena:  {}{}{}'.format('\033[7;34m', dez, '\033[m'))
print('Centena: {}{}{}'.format('\033[1;35m', cent, '\033[m'))
print("Milhar:  {}{}{}".format('\033[4;41m', mil, '\033[m'))