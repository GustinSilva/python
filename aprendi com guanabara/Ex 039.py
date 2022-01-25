"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
se ele ainda vai se alistar
se é a hora de se alistar
se já passou o tempo de alistar

o programa também deve falar o tempo que falta ou que passou
"""
import datetime
import time

ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc
print('Um momento estamos fazendo o calculo.\n', end='')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
if idade == 18:
    print('Quem nasceu no ano de {} tem {} anos em {}'.format(ano_nasc, idade, ano_atual))
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade > 18:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
    print('Seu alistamento deu-se em {}.'.format(ano_nasc+18))
else:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))
    print('Ainda faltam {} anos para seu alistamento.'.format(18-idade))
    print('Seu alistamento será em {}.'.format(ano_nasc+18))
