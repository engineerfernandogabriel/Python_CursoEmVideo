# Faça um programa que leia um número e mostre na tela o seu sucessor e seu antecessor

num1 = int(input('Digite um número: '))

numsucessor = num1 + 1

numantecessor = num1 - 1

print('O sucessor de {} é {} e o seu antecessor é {}' .format(num1, numsucessor, numantecessor))
