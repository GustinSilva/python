"""
Crie um programa que leia uma frase e diga se ela é um palindromo, a mesma coisa de frente pra tras e tras pra frente
desconsiderando os espaços
"""

frase = input('Diga uma frase: ').strip().upper()
palavras = frase.split()
palin = ''.join(palavras)
inverso = palin[::-1]
print(f'O inverso de {palin} é {inverso}.')
if palin == inverso:
    print('Temos um Palindromo!!!')
else:
    print('A frase digitada não é um Palindromo.')
