"""
Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3 e estão entre 1 e 500
"""
intervalo = int(input('Final do Intervalo: '))
soma = 0
print('Foram somados os números: ')
for c in range(0, intervalo+1):
    if c % 3 == 0 and c % 2 == 1:
        soma = soma + c
        print(c, end='  ')
print('\n\nO valor da soma é {}'.format(soma))
