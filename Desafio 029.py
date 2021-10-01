#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada Km acima do limite

vcar = float(input('Qual a velocidade do carro: '))

if vcar < 81:
    print('Tenha uma Boa viagem, use cinto de segurança')
else:
    excedido = vcar - 80
    multa = (vcar - 80) * 7
    print('Você excedeu o limite de velocidade em {} Km/h' .format(excedido))
    print('Sua multa é de R$ {:.2f}' .format(multa))
    