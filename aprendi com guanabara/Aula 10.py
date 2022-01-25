num1 = float(input('Digite a nota um: '))
num2 = float(input('Digite a nota dois: '))
med = (num1 + num2) / 2
print('A sua média de notas foi {:.1f}'.format(med))
if med >= 6.0:
    print('Sua média foi boa, parabéns!!!')
else:
    print('Precisa estudar mais!!!')

