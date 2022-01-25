"""
Crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuário digitar 999, condição de parada
mostre no final quantos numeros digitados e qual a soma entre eles
"""
valor = cont = soma = maior = menor = 0
while True:
    valor = int(input('Digite um valor [999 para sair]: '))
    if valor == 999:
        break
    else:
        soma += valor
        cont += 1
        if cont == 1:
            maior = menor = valor
        elif maior < valor:
            maior = valor
        elif menor > valor:
            menor = valor
print(f'Foram digitados {cont} valores, e a soma é {soma}')
print(f'O maior valor digitado é {maior} e o menor valor é {menor}')

