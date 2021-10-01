#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

distviagem = float(input('Qual a distância da sua viagem em Km: '))

if distviagem < 201:
    valor1 = distviagem * 0.50
    print('O valor da sua passagem é de R$ {:.2f}' .format(valor1))
else:
    valor2 = distviagem * 0.45
    print('O valor da sua passagem é de R$ {:.2f}' .format(valor2))
