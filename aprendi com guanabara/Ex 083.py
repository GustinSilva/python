"""
Crie um programa onde o usuário digite uma expressão quaquer que use parenteses
o aplicativo tem de analisar se a expressao esta com parenteses abertos e fechados na ordem correta
"""
chave = []
expressao = input('Digite a expressão: ')
for v in expressao:
    if v == '(':
        chave.append('(')
    elif v == ')':
        if len(chave) > 0:
            chave.pop()
        else:
            chave.append(')')
            break
if len(chave) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
