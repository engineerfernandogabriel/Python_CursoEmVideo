#Faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra A
#em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip()

minfrase = frase.lower()

a = minfrase.count('a')

prima = int(minfrase.find('a'))

ultima = int(minfrase.rfind('a'))

print('A letra A aparece: {} vezes' .format(a))

print('A primeira letra A apareceu na posição {}' .format(prima+1))

print('A última letra A aparece na posição: {}' .format(ultima+1))
