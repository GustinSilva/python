"""
\033[  Style ; Text ; Back   m

Style 0 Nada, 1 , 4 Sublinhado, 7 Tachado
Text 30 Branco, 31 Vermelho,32 Verde, 33 Amarelo, 34 Azul, 35 Roxa, 36 Azul, 37 Cinza
Back 40 Branco, 41 Vermelho, 42 Verde, 43 Verde, 44 Azul, 45 Roxa, 46 Azul, 47 Cinza
"""

# Da biblioteca tal, posso importar só um comando, ai facilita e economiza memoria
from math import trunc
import random

#pode usar o randint e randrange, mas ambos só geram numeros aleatórios inteiros
#random.random só geral numeros reais entre 0 e 1
num = random.randrange(1, 500)
digitado = float (input('Digite um número: '))
print('Foi digitado o número {}, e sua parte inteira é {}.\nAo mesmo tempo o computador pensou em {}.'.format(digitado, trunc(digitado),num))


# print(\'Foi digitado o número {} e sua parte inteira é {}\'.format(digitado, int(digitado)))
