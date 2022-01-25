"""
Faça um programa que mostre a tabuada de vários numeros, um de cada vez para o valor digitado pelo usuario
o programa será interrompido quando o valor digitado for negativo
"""
while True:
    valor = int(input('Qual tabuada deseja ver [valor negativo para parar]: '))
    if valor < 0:
        break
    print('-' * 25)
    for contador in range(0, 11):
        print(f'{valor} x {contador} = {valor * contador}')
    print('-' * 25)
print('Programa de tabuada ENCERRADO! Obrigado por participar!')
