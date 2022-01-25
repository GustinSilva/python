"""
Escreva um programa que leia um número inteiro e peça ao usuário que escolha a base de transformação
1 binário (pega números e divide por 2, os restos se 0 ou 1 escreve ao contrário, ver aula Prof. MURAKAMI
2 octal
3 hexadecimal
"""
import time
print('-=' * 20)
print('   BEM VINDO AO SUPER CONVERSOR NOSSO')
print('-=' * 20)
num = int(input('Digite um número: '))
opcao = int(input("""Digite a conversão desejada:
    [1] Binário
    [2] Octal
    [3] Hexadecimal """))

if opcao == 1:
    convertido = str(bin(num))
elif opcao == 2:
    convertido = str(oct(num))
elif opcao == 3:
    convertido = str(hex(num))
else:
    print('Por gentileza selecione uma das opções indicadas!!!')

if opcao == 1 or opcao == 2 or opcao == 3:
    print('\nPor gentileza, aguarde um pouco até terminarmos nosso serviço...')
    time.sleep(2)
    print('Estamos Quase terminando...')
    time.sleep(2)
    print('\033[36m\nProntinho! Obrigado por aguardar...\033[m')
    time.sleep(1.5)
    print('\nO número {} convertido é {}'.format(num, convertido))
