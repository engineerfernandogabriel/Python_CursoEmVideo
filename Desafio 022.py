#Cire um programa que leia o nome completo de uma pessoa e mostre
#O nome com todas as letras maisculas
#O nome com todas minusculas
#Quantas letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()

maisculo = nome.upper()

minusculo = nome.lower()

totalletras = len(nome) - nome.count(' ')

separarnome = (nome.split())

primeironome = int(len(separarnome[0]))

print('Tudo Maisuculo: {}' .format(maisculo))

print('Tudo Mínusculo: {}' .format(minusculo))

print('Total de Caracteres: {} ' .format(totalletras))

print('Primero nome tem: {} caracteres' .format(primeironome))
