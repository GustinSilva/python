lista = [int(input(f'Digite um valor: ')) for c in range(0, 5)]  # ou então pode ser lista = list()
lista.append(4)
lista.append(45)
lista.append(56)
lista.append(41)
print(lista)
lista[2] = 2
print(lista)

num = [4, 12, 5, 9, 1]
num[3] = 3
print(num)
num.append(11)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(6, 11)
num.remove(11)
print(num)
if 24 in num:
    num.remove(24)
else:
    print('Não achei o numero 24')
print(num, '\n\n')

valor = []
valor.append(4)
valor.append(35)
valor.append(5)
for c in range(0,5):
    valor.append(int(input('Digite um valor: ')))

print(valor)
for v in valor:
    print(f'{v} ... ', end='')
print('')
for v in valor:
    print(f'{valor} ;;; ', end='')
print('')
for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei o valor {v}!')
valor.sort()
for c, v in enumerate(valor):
    print(f'Na posição {c} temos em ordem {v}!!')

print('')
a = [2, 3, 7, 5, 9]
c = a[:]  # assim ele recebe so os elementos da lista
b = a  # assim python faz ligação de uma lista a outra e toda alteração é compartilhada
b[2] = 15

print(f'A lista A: {a}')
print(f'A lista B: {b}')
print(f'A lista C: {c}')