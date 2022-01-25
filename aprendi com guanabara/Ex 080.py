"""
Crie um programa que o usuário digite 5 valores e os cadastre em uma lista
já na posição correta
sem usar o sort()
no final mostre a lista ordenada
"""
lista = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        cont = 0
        while cont in range(0, len(lista)):
            if valor <= lista[cont]:
                lista.insert(cont, valor)
                break
            cont += 1
print('-=' * 35)
print(f'Os valores digitados foram {lista}.')
