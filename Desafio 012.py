#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

original = float(input('Qual o valor do produto sem desconto: R$ '))

desconto = original * 0.95

print('O preço do produto com desconto de 5% é R$ {:.2f}' .format(desconto))
