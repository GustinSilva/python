"""
Faça um programa que leia nome e media de um aluno
guarda a a situação em um dicionario. no final mostra o conteudo da estrutura na tela
"""
dados = dict()
nome = input('Nome: ').title().strip()
dados['nome'] = nome
media = float(input(f'Média de {nome}: '))
dados['media'] = media
print(f'Nome é igual a {dados["nome"]}.')
print(f'Média é igual a {dados["media"]}.')
if dados['media'] >= 7:
    print('Situação é igual a Aprovado.')
else:
    print('Situação é igual a Reprovado.')
