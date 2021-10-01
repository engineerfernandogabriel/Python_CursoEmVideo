#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salarioatual = float(input('Digite o salário atual: R$ '))

salariofuturo = salarioatual * 1.15

print('Com aumento de 15% o salário passará de R${:.2f} para R${:.2f}'.format(salarioatual, salariofuturo))
