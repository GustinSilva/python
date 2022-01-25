"""
Faça um progrma que tenha função maior
recebe vários parametros e analisa todos os valores e diz qual deles é o maior
"""
from random import randint
from time import sleep

def maior (lst):
    quant = randint(3, 7)
    for c in range(quant):
        lst.clear()
        cont = randint(1, 10)
        for c in range(cont):
            lst.append(randint(0, a))
        print('-=' * 35)
        print('Analisando os valores ... ')
        for d in range(cont):
            print(f'{lst[d]}..', end='')
            sleep(0.3)
        print(f'Foram informados {len(lst)} valores ao todo. ')
        print(f'O maior valor informado foi {max(lst)}.')


lista = []
a = int(input('Valor limite: '))
maior(lista)