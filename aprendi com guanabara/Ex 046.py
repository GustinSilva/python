"""
Crie um programa que faça uma contagem regressiva para os estouros de fogos de artificio de 10 ate 0...
com pausa de 1 seg
"""
import time

for c in range(10, -1, -1):
    print(c, '...')
    time.sleep(1)

print('Aêeeeee!!! Boommmm!!! Poowwww!!!')
