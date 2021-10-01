#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere U$$1.00=R$3.27

cart = float(input('Quanto dinheiro você tem na carteira: R$ '))

dolar = 3.27

cash = cart/dolar

print('Você pode comprar US$ {:.2f} ' . format(cash))
