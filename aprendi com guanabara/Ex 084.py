"""
Faça um programa que leia nome e peso de várias pessoas, guarde tudo em uma lista no fim mostre
quantos foram cadstrados
uma lista com os mais pesados
uma lista com os mais leves
"""
pessoas = list()
dados = list()
cont = 0
while True:
    dados.append(input('Diga o nome: '))
    dados.append(int(input('Diga o peso: ')))
    pessoas.append(dados[:])
    if cont == 0:
        pesado = leve = dados[1]
    else:
        if pesado < dados[1]:
            pesado = dados[1]
        elif leve > dados[1]:
            leve = dados[1]
    dados.clear()
    cont += 1
    continua = input('Deseja continuar: ').upper()
    if continua == 'N':
        break
for c in pessoas:
    if pesado == c[1]:
        print(c)
print(pessoas, pesado)