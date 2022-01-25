"""
if
elif
elif
else
"""

nome = str(input('Qual é o seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Lais Jéssica Juliana':
    print('Que nome feminino bonito.')
else:
    print('Seu nome é bem normal;')
print('Tenha um bom dia, {}{}{}!'.format('\033[35m', nome.capitalize(), '\033[m'))
