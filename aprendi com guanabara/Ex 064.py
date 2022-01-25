"""
Crie um programa que leia vários numeros inteiros. o programa só vai parar quando ler o numero 999 que e condição de parada
mostre a soma entre eles e quantos numeros foram digitados
"""
resposta = 0
soma = 0
termos = 0
print('Bem Vindo ao Valores Média e Somatórios')
print('^' * 40)
while resposta != 999:
    resposta = float(input('Diga um valor para continuar [999 para sair]: '))
    if resposta == 999:
        print('SAIR')
    else:
        soma += resposta
        termos += 1
print(f'Foram digitados {termos} termos, a soma é {soma} e a sua média é de {soma/termos:.2f}. Desconsiderado o exit.')

