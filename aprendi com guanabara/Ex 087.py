"""
Aprimore o desafio anterior e mostre
a soma de todos os valores pares
a soma dos valores da terceira coluna
o maior valor da segunda linha
"""
matriz = [[], [], []]
soma = somaTerceira = maiorSegunda = 0
for c in range(0, 3):
    for d in range(0, 3):
        temp = int(input('Diga um valor: '))
        matriz[c].append(temp)
        if temp % 2 == 0:
            soma += temp
        if d == 2:
            somaTerceira += temp
for a in range(0, 3):
    print(*matriz[a])
print(f'Todos os pares somados são {soma}.')
print(f'Os valores da Terceira coluna somados são {somaTerceira}.')
print(f'O maior valor presente na segunda linha é {max(matriz[1])}')
