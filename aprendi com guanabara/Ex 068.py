"""
Faça um programa que jogue par ou impar com o computador, o jogo será interrompido quando o jogador perder.
mostra o numero de vitorias consecutivas que ele conseguiu
"""
contador = 0
from random import randint
print('-=' * 25)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 25)
while True:
    valor = int(input('Diga um valor: '))
    par_impar = input('Par ou Ímpar: [P/I] ')
    computador = randint(0, 25)
    soma = valor + computador
    if soma % 2 == 0 and par_impar in 'Pp':
        print('-' * 25)
        print(f'Você jogou {valor} e o computador {computador}. Total deu {soma}, DEU PAR!!!')
        print('-' * 25)
        contador += 1
    elif soma % 2 == 1 and par_impar in 'Ii':
        print('-' * 25)
        print(f'Você jogou {valor} e o computador {computador}. Total deu {soma}, FOI ÍMPAR!!!')
        print('-' * 25)
        contador += 1
    else:
        print('-' * 25)
        print(f'Você jogou {valor} e o computador {computador}. Total deu {soma}, DEU {"IMPAR" if soma % 2 == 1 else "PAR"}')
        print('-' * 25)
        break
print('VOCÊ PERDEU!')
print('-=' * 25)
print(f'GAME OVER! Você venceu {contador} {"vez" if 0 <= contador <= 1 else "vezes"}')
