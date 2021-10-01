#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num1 = int(input('Digite um número: '))

print('Dado o número {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.5f}' .format(num1, (num1*2), (num1*3), (num1**(1/2))))
