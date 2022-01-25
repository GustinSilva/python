"""
Crie um programa que gerencie o aproveitamento do jogador.
o programa vai ler o nome e quantos jogos. depois quantos gols em cada partida
no final guarda em um dicionario incluindo o total de gols feitos durante o campeonato
"""
dados = {}
gol = []
dados['nome'] = input('Nome do jogador: ').title().strip()
jogos = int(input(f'Quantas partidas {dados["nome"]} jogou: '))
for c in range(0, jogos):
    gol.append(int(input(f'    Quantos gols na partida {c+1}: ')))
dados['gols'] = gol [:]
dados['total'] = sum(gol)
print('-=' * 25)
print(dados)
print('-=' * 25)
for c, v in dados.items():
    print(f'O campo {c} tem o valor {v}.')
print('-=' * 25)
print(f'O jogador {dados["nome"]} jogou {jogos} partidas.')
for d, e in enumerate(dados['gols']):
    print(f'    => Na partida {d+1}, fez {e} gols.')
print(f'Foi um total de {dados["total"]} gols.')
