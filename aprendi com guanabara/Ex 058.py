"""
Melhore o jodo do Desafio 28onde o computador pensa em um número de 0 a 10, e que agora o jogador tenta acerta, e
o computador vai até adivinhar, e no final mostra quandos palpites foram necessários
"""
import random
computador = random.randint(0, 10)
cont = 0
tentativa = 12
while tentativa != computador:
    tentativa = int(input('Diga seu palpite, entra 0 e 10: '))
    if tentativa not in range(0, 11):
        print('Essa não foi uma tentativa válida, gentileza ajustar seu palpite.\n')
    else:
        if tentativa == computador:
            print('\nParabéns, você acertou o número que pensei.')
            cont += 1
        else:
            print('Não foi esse o valor que eu pensei.\n')
            cont += 1
print(f'Pensei no número {computador}, e você gastou {cont} tentativas para acertar.')
