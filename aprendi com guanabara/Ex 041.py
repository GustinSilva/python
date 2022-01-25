"""
A confederação de natação precisa de um programa que leia o ano de nascimento e mostre a categoria
ate 9 anos Mirim
até 14 anos Infantil
até 19 anos Junior
ate 20 anos Senior
acima Master
"""
import datetime
nascimento = int(input('Ano de nascimento:'))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento

if idade < 9:
    print('O nadador está na categoria MIRIM.')
elif 9 < idade < 14:
    print('O nadador está na categoria INFANTIL.')
elif 14 < idade < 19:
    print('O nadador está na categoria JUNIOR.')
elif 19 < idade < 20:
    print('O nadador está na categoria SENIOR.')
else:
    print('O nadador já se enquadra na categoria MASTER.')
print('O Atleta possui {} anos nesse momento.'.format(idade))