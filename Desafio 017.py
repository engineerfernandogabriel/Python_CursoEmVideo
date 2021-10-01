#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcue e mostre
#o comprimento da hipotenusa

'''import math

co = float(input('Digite o valor do cateto oposto: '))

ca = float(input('Digite o valor do cateto adjacente: '))

hi = math.hypot(co, ca)

print('O valor da hipotenusa é {:.2f}' .format(hi))'''

from math import hypot

co = float(input('Digite o valor do cateto oposto: '))

ca = float(input('Digite o valor do cateto adjacente: '))

hi = hypot(co, ca)

print('O valor da hipotenusa é {:.2f}' .format(hi))
