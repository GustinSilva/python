"""
Faça um programa com a função escreva que recebe um texo qualquer
e mostra a mensagem adapatavel ao tamanho do texto
"""
def escreva(a):
    print('~' * (len(a)+4))
    print(f' {a}')
    print('~' * (len(a)+4))


while True:
    letra = input('Diga a frase: ')
    escreva(letra)
    cont = input('Continuar [S/N]: ').upper().strip()
    if cont == 'N':
        break