"""
Faça um programa que tenha uma função contador .. receba 3 parametros
inicio fim e passo
o programa deve contar:
de 1 ate 10, de 1 em 1
de 10 ate 0 de 2 em 2
uma contagem personalizada.
"""
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if f > i:
        cont = i
        while cont <= f:
            print(f'{cont}.. ', end='')
            cont += p
            sleep(0.2)
        print('FIM!!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}.. ', end='')
            cont -= p
            sleep(0.5)
        print('FIM!!!')
    print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)