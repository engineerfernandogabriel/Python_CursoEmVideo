#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

computador = randint(0,5)

print('JOGO DA ADIVINHAÇÃO')
print('ENTRE O e 5, ADIVINHE QUAL ESCOLHI')

numplay = int(input('Em que número pensei ?'))

print('PROCESSANDO ...')

sleep(1) #tempo entre parênteses está em segundos

if numplay != computador:
    print('PERDEU ! Eu pensei no número {} e não no {}' .format(computador, numplay))
else:
    print('PARABÉNS, VOCÊ ACERTOU!')

