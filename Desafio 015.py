#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

kminicial=float(input('Digite o Km inicial: '))

kmfinal=float(input('Digite o Km final: '))

kmusado= kmfinal - kminicial

diasusados = int(input('Digite a quantidade de dias de utilização dos carro: '))

valordia = diasusados * 60

valorkm = kmusado * 0.15

print('O valor a ser pago pelas diárias é R$ {:.2f} e pelos Km utilizados R$ {:.2f}' .format(valordia, valorkm))
print('O valor total é R$ {:.2f}' .format(valordia+valorkm))
