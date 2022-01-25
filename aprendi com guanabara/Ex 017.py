#importei apenas comandos específicos da biblioteca math, raiz quadrada SQRT, e potencia POW
from math import sqrt, pow

catad = float(input('Digite o Cateto Adjacente: '))
catop = float(input('Digite o Cateto Oposto: '))

#Hipotenusa é a soma do quadrado dos catetos
hip = sqrt(pow(catad, 2)+pow(catop, 2))
# hip = math.hypot(catad, catop)

print('Triângulo de Catetos {:.2f} e {:.2f}, sua hipotenusa é {:.2f}'.format(catad, catop, hip))