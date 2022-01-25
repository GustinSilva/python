#não aceitou importar apenas o randint da biblioteca Random, tive de importar toda ela
from math import sin, cos, tan, radians
import random

angdig = float(input('Digite um ângulo: ')) #Digitado
angpc = float(random.randint(1, 360)) #Computador escolhe no intervalo

#mudar os angulos para radianos
print('O humano pensou em {}º:\nSeno {:.3f}\nCosseno {:.3f}\nTangente {:.3f}'.format(angdig, sin(radians(angdig)), cos(radians(angdig)),tan(radians(angdig))))
print('O PC pensou em {}º:\nSeno {:.3f}\nCosseno {:.3f}\nTangente {:.3f}.'.format(angpc, sin(radians(angpc)), cos(radians(angpc)), tan(radians(angpc))))
