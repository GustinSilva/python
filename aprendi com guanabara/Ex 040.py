"""
Crie um programa que leia duas notas do aluno e diga
média abaixo de 5 reprovado
media entre 5 e 6,9 recuperação
media 7 ou superior aprovado
"""

nota1 = float(input('Valor da 1ª nota: '))
nota2 = float(input('Valor da 2ª nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Sua nota média foi de {} pts, abaixo de 5.0, você foi \033[4;31mReprovado\033[m.'.format(media))
elif 5 < media < 6.99:
    print('Sua nota média foi de {} pts, está de \033[4;35mRecuperação\033[m.'.format(media))
else:
    print('Sua nota média foi de {} pts, está \033[4;36mAprovado\033[m.'.format(media))
