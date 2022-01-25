"""
Crie um programa que leia o comprimento de 3 retas e diga se elas formam um triangulo
"""
cores = {'limpa': '\033[m',
         'roxo': '\033[35m',
         'vermelho': '\033[31;43m',
         'pretoebranco': '\033[7;34m'}

print('-=' * 20)
print('     Analisador de Triangulos')
print("-=" * 20)

reta1 = float(input('Diga o comprimento da reta 1: '))
reta2 = float(input('Diga o comprimento da reta 2: '))
reta3 = float(input('Diga o comprimento da reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    perim = reta1 + reta2 + reta3
    print('\nAs medidas informadas formam um triangulo de perímetro {}{}{} unidades.'.format(cores['roxo'], perim, cores['limpa']))
else:
    print('\nAs medidas informadas {}{}{} são capazes de formar um triangulo, tente novamente!!!'.format(cores['pretoebranco'],'não', cores['limpa']))
