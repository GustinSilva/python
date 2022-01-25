"""
\033[  Style ; Text ; Back   m

Style 0 Nada, 1 , 4 Sublinhado, 7 Tachado
Text 30 Branco, 31 Vermelho,32 Verde, 33 Amarelo, 34 Azul, 35 Roxa, 36 Azul, 37 Cinza
Back 40 Branco, 41 Vermelho, 42 Verde, 43 Verde, 44 Azul, 45 Roxa, 46 Azul, 47 Cinza
"""

print('\033[0;30;41m Olá, Mundo!!! \033[m')
print('\033[0;31;42m Olá, Mundo!!!\033[m')
print('\033[4;33;44m Olá Mundo!!! \033[m')
print('\033[7m Olá Mundo!!! \033[m')
print('\033[7;35m Olá Mundo!!! \033[m')
