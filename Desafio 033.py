#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

print('DIGITE 3 NÚMEROS E VAMOS ORDENAR EM ORDEM CRESCENTE')

a = int(input('Digite o primeiro valor: '))

b = int(input('Digite o segundo valor: '))

c = int(input('Digite o terceiro valor: '))

#Verificando o menor número

menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

#Verificando qual o maior número

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print('O menor valor digitado é {}' .format(menor))
print('O maior valor digitado é {}' .format(maior))
