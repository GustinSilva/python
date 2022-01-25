"""
Crie um programa onde o usuário digite sete valores numericos e os cadastre em uma unica lista que os separe em par e impar
no fim mostre os valores pares e os impares
"""
lista = [[], []]
temp = 0
for c in range(0, 7):
    temp = int(input('Digite um valor: '))
    if temp % 2 == 0:
        lista[0].append(temp)
    else:
        lista[1].append(temp)
lista[0].sort()
lista[1].sort()
print(f'Os números pares digitados foram {lista[0]}.')
print(f'Os valores ímpares digitados foram {lista[1]}.')
