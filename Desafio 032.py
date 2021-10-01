#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

'''Comando para importar o ano atual:
from datetime import date
ano = date.today().year -> recebe apenas o ano da data atual '''

ano = int(input('Digite um ano para saberm se é bissexto: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto' .format(ano))
else:
    print('O ano {} NÃO é Bissexto' . format(ano))
    