"""
Crie um programa que leia vários numeros e coloca em uma lista
depois mostre
quantos numeros foram digitados
a lista de valores em ordem decrescente
se o valor 5 foi digitado e está ou não na lista
"""
lista = []
quant = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    continua = input('Quer continuar: ').upper()
    quant += 1
    if continua in 'N':
        break
emOrdem = lista[:]
print(f'Foram digitados {quant} números.')
emOrdem.sort()
print(f'Os números em ordem crescente são {emOrdem}')
emOrdem.sort(reverse=True)
print(f'Os valores em lista decrescente são {emOrdem}')
if 5 in lista:
    print(f'O valor 5 está na lista, na posição {lista.index(5)}')
print(lista)
