#Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeio e o ultimo nome separadamete

nome = str(input('Digite o seu nome completo: ')).strip()

maisculo = nome.upper()

splitado = maisculo.split()

prinome = splitado [0]

ultimonome = splitado [len(splitado)-1]

print('O seu primeito nome é: {}' .format(prinome))

print('O seu último nome é: {}' .format(ultimonome))
