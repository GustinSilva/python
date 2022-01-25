"""
Aprimore o desafio 093 para que funcione com vários jogadores. incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador
"""
dados = {}
gol = []
lista = []
while True:
    print('-' * 35)
    dados['nome'] = input('Nome do jogador: ').title().strip()
    cont = int(input('Quantos jogos: '))
    for c in range(0, cont):
        gol.append(int(input(f'   Gols na partida {c+1}: ')))
    dados['gols'] = gol[:]
    gol.clear()
    lista.append(dados.copy())
    segue = input('Deseja continuar: [S/N] ').upper()
    if segue == 'N':
        break
print('-=' * 25)
print(f'{"cod":<4}{"nome":<15}{"gols":<10}{"total":<6}')
print('-' * 40)
for k, p in enumerate(lista):
    print(f'{k:^4}{p["nome"]:<15}{p["gols"]}')
print('-' * 40)
while True:
    mostrar = int(input('Mostrar dados de qual jogador: '))
    if mostrar == 999:
        break
    if mostrar >= len(lista):
        print(f'Erro! não existe jogador com código {mostrar}! Tente novamente!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[mostrar]["nome"]}')
        for d, e in enumerate(lista[mostrar]["gols"]):
            print(f'Na partida {d} fez {e} gols.')
        print('-' * 40)
print('ENCERRANDO. . .')

