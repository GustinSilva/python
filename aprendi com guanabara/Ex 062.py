"""
Melhore o desafio 51 perguntando se o usuário deseja continuar, e quantos termos a mais ele deseja,
o programa encerra quando o usuário disser que deseja mostrar Zero termos a mais
"""
termo = float(input('Termo inicial: '))
razao = float(input('Razão da PA: '))
inicial = int(input('Quantos termos iniciais: '))
cont = 1
num_ter = 0
while inicial != 0:
    while cont <= inicial:
        print(f'{termo} -> ', end='')
        cont += 1
        termo += razao
        num_ter += 1
    print('Pausa')
    inicial = int(input('Quantos termos mais devo mostrar: '))
    cont = 1
print(f'Progressão finalizada com \033[4;34m{num_ter}\033[m termos apresentados. FIM!!!')


