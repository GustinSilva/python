"""
Funções
"""
#Caso 01:
#def mostraLinha():
#    print('-' * 30)
#mostraLinha()

#Caso 02:uso de funções
#def mensagem(msg):
#    print('-' * 50)
#    print(msg)
#    print('-' * 50)
#mensagem('Sistema de Aluno')
#mensagem('Aprenda Python')
#mensagem('Estudar')

#Caso 03: função com comprimentp
#def mensagem(txt):
#    print('-' * len(txt))
#    print(len(txt))
#mensagem('Socorro Ave Maria')

#Caso 04: Parametros
#def soma (a, b):
#    s = a + b
#    print(s)
#    print(f'A = {a} e B = {b}')
#soma(4, 5)
#soma(6, 3)
#soma(b=5, a=12)

#Caso 05: Empacotar parametros
#def contador(*num):   # o sinal * é desempacotar... cria tuplas com os valores
#    for valor in num:
#        print(f'{valor}', end='')
#    print('\n', len(num))
#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

#Caso 06: Empacotar valores, com tuplas
#def contador(*num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} valores.')
#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

#Caso 07: LIstas e dobra valor
#def dobra(lst):
#    pos = 0
#    while pos < len(lst):
#        lst[pos] *= 2
#        pos += 1
#valores = [6, 3, 9, 1, 0, 2]
#print(valores)
#dobra(valores)
#print(valores)

#Caso 08:
#def soma(*valores):
#    s = 0
#    for num in valores:
#        s += num
#    print(f'Somando os valores {valores} temos {s}.')
#soma(5, 2)
#soma(6, 5, 9, 10)


