"""
Crie um programa que leia vários numeros e coloque em uma lista
depois crie duas listas que recebam apenas os pares ou os impares
e mostre as 3 listas
"""
lista = list()
par = list()
impar = list()
conta = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = input('Deseja continuar [S/N]: ').upper()
    if cont in 'nN':
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v:
        impar.append(v)
print(f'A lista completa é {lista}')
print(f'Os valores pares são {par}')
print(f'Os valores impares são {impar}')
