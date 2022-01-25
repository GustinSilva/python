"""
Crie um programa que aprove um emprestimo bancário, onde o programa leia:
Valor da Casa / salário da pessoa / quantos anos será o pagamento

Calcule o valor da prestação mensal, sabendo que ela não pode ser superior a 30% da renda da pessoa, se passar o
emprestimo será negado
"""
import time
valor_casa = float(input('Valor do imóvel que deseja comprar: '))
salario = float(input('Qual o salário do pagador: '))
anos_pagamento = int(input('Quantos anos para pagar: '))
meses_pagamento = int(input('Quantos meses para pagamento: '))

tempo_pagamento = anos_pagamento * 12 + meses_pagamento

prestacao = valor_casa / tempo_pagamento
print('\nValor do imóvel de R$ {:.2f}, salário R$ {:.2f}, tempo do emprestimo de {} meses.\n'.format(valor_casa, salario, tempo_pagamento))
time.sleep(3)

if prestacao > salario * 0.3:
    print('Infelizmente o empréstimo não pode ser concedido, a prestação supera {}{}{} da renda mensal.'.format('\033[36m', '30%', '\033[m'))
else:
    print('Podemos conceder o empréstimo para o senhor!!!')

print('A parte da renda que será comprometida é de {}{:.1%}{}.'.format('\033[31m', (prestacao/salario), '\033[m'))
