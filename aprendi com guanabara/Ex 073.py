"""
Crie uma tupla preenchida com os 20 primeiros colocados do campeonato brasileiro na ordem de colocação e mostre
os 5 primeiros colocados
os 4 ultimos colocados
uma lista com os times em ordem alfabetica
em que posição está a chapecoense
"""
colocacao = ('Atletico-MG', 'Palmeiras', 'Bragantino', 'Fortaleza', 'Flamengo', 'Internacional', 'Corinthians', 'Fluminense',
             'Atletico-GO', 'America-MG', 'Cuiabá', 'Atletico-PR', 'São Paulo', 'Ceará', 'Bahia', 'Santos',
             'Juventude', 'Sport', 'Gremio', 'Chapecoense')
print(colocacao[:6])  # imprime os 5 primeiros
print(colocacao[-4:])  # imprime os 4 ultimos começa do -4 ate o ultimo
print(sorted(colocacao))  # sorted .... coloca ordem alfabetica a listagem
print(f'A chapecoense está na {colocacao.index("Chapecoense")+1}ª colocação.')   # indicação da posição do elemento pesquisado
