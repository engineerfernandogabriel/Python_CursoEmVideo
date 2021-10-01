#Desenvola um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

print('--- ANALISADOR DE TRIÂNGULOS ---')

seg1 = float(input('Digite o valor do primeiro segmento: '))

seg2 = float(input('Digite o valor do segundo segmento: '))

seg3 = float(input('Digite o valor do terceiro segmento: '))

if (seg1 + seg2) > seg3 and (seg2 + seg3) > seg1 and (seg3 + seg1) > seg2:
    print('Estes segmentos podem formar um Triângulo')
else:
    print('Estes segmentos NÃO PODEM formar um Triângulo')
