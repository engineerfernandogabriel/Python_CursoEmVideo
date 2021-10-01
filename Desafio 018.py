#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

'''import math

ang = float(input('Digite um ângulo: '))

angrad = math.radians(ang)

seno = math.sin(angrad)

cosseno = math.cos(angrad)

tangente = math.tan(angrad)

print('O ânguo de {} tem \nSeno de {:.2f} \nCosseno de {:.2f} \nTangente de {:.2f}' .format(ang, seno, cosseno, tangente))'''


from math import radians, sin, cos, tan

ang = float(input('Digite um ângulo: '))

angrad = radians(ang)

seno = sin(angrad)

cosseno = cos(angrad)

tangente = tan(angrad)

print('O ânguo de {} tem \nSeno de {:.2f} \nCosseno de {:.2f} \nTangente de {:.2f}' .format(ang, seno, cosseno, tangente))
