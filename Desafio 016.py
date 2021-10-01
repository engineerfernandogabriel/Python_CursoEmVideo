#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
#Ex. digite um número 6.127. O número 6.127 tem a parte inteira 6

'''
num = int(input'Digite um número: '))

print('A parte inteira do número {} é {}' .format(num, int(num)))
'''

import math

numreal = float(input('Digite um valor numérico: '))

numint = math.trunc(numreal)

print('A parte inteira do número {} é {}' .format(numreal, numint))
