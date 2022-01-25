"""
Crie um programa que leia dois valores e mostre o menu onde escolhe 1 somar, 2 multiplicar 3 maior
4 novos valores 5 sair do programa
seu programa deverá realizar a operação solicitada em cada caso
"""
valor1 = float(input('Diga o 1º valor: '))
valor2 = float(input('Diga o 2º valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input("""\nQual operação deseja:
    [1] SOMAR 
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS VALORES
    [5] SAIR DO PROGRAMA 
    >>>>> Opção desejada: """))
    if opcao not in range(1,6):
        print('\nOpção inválida, gentileza escolha um valor das opções indicadas.')
        print('-=' * 35)
    else:
        if opcao == 1:
            print(f'A soma {valor1} + {valor2} = {valor1+valor2}')
            print('-=' * 15)
        elif opcao == 2:
            print(f'O produto {valor1} x {valor2} = {valor1*valor2}')
            print('-=' * 15)
        elif opcao == 3:
            print(f'O maior valor digitado é {max(valor2,valor1)}')
            print('-='*15)
        elif opcao == 4:
            valor1 = float(input('Diga o novo 1º valor: '))
            valor2 = float(input('Diga o novo 2º valor: '))
            print('-=' * 15)
print('\nObrigado por participar. Volte sempre!!!')


