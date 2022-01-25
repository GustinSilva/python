"""
\033[  Style ; Text ; Back   m

Style 0 Nada, 1 , 4 Sublinhado, 7 Tachado
Text 30 Branco, 31 Vermelho,32 Verde, 33 Amarelo, 34 Azul, 35 Roxa, 36 Azul, 37 Cinza
Back 40 Branco, 41 Vermelho, 42 Verde, 43 Verde, 44 Azul, 45 Roxa, 46 Azul, 47 Cinza
"""

nome = input('\033[4m Digite seu nome: \033[m')
print('É um prazer conhecer você \033[7;32m{}\033[m!!!'.format(nome))
