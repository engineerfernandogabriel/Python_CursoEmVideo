#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

num = int(input('Digite um número inteiro: '))

resultado = num % 2

if resultado == 0:
    print('{} é um número PAR' .format(num))
else:
    print('{} é um número ÍMPAR' .format(num))
