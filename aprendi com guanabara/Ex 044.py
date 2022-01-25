"""
Elabore um programa que calculo o valor a ser pago por um produto
considere o preço normal e a condição de pagamento
a vista dinheiro ou cheque com 10% de desconto
a vista no cartão 5% de desconto
em até 2x no cartão preço normal
3x ou mais no cartão 20% de juros
"""
valor = float(input('Preço do produto: (R$) '))
pagamento = int(input("""Forma de pagamento:
[1] A vista, dinheiro ou cheque
[2] A vista, cartão
[3] 2x no cartão
[4] 3x ou mais no cartão """))
print('\n')
if pagamento == 1:
    print('Valor nesse modo de pagamento, com 10% de desconto no dinheiro é de R$ {:.2f}.'.format(valor*0.9))
elif pagamento == 2:
    print('Valor nesse modo de pagamento, com 5% de desconto no cartão, é de R$ {:.2f}.'.format(valor*0.95))
elif pagamento == 3:
    print('Valor nesse modo de pagamento, 2x sem desconto no cartão {}.'.format(valor))
else:
    print('Valor nesse modo de pagamento, 3x no cartão, com 20% de juros, é de R$ {:.2f}.'.format(valor*1.2))
