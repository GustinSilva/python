"""
Crie um programa que tenha uma tupla com nomes de produtos e respectivos preços, na sequencia.
No final mostre uma listagem de preços organizando os dados de forma tabular
"""
produto = ('Arroz', 17.99, 'Maça', 2.59, 'Feijao', 5.99, 'Batata', 4.59, 'Jiló', 3.69, 'Cenoura', 4.19, 'Leite', 3.69,
           'Macarrão', 2.69)
print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
for c in range(0, len(produto), 2):
    print(f'{produto[c]:.<40}', 'RS', f'{produto[c+1]:>5}')
