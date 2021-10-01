#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00 calcule um aumento de 10%
#Para os infeiroes ou iguais o aumento é de 15%

salatual = float(input('Qual o seu salário atual R$ '))

if salatual >= 1250:
    salnovo1 = salatual * 1.1
    print('Você receberá um aumento de 10%')
    print('Seu novo salário é R$ {:.2f}' .format(salnovo1))
else:
    salnovo2 = salatual * 1.15
    print('Você receberá um aumento de 15%')
    print('Seu novo salário é R$ {:.2f}' .format(salnovo2))
