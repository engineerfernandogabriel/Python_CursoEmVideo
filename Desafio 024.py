#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digeite o nome da cidade: ')).strip()

min = cidade.lower() 

separar = min.split()

print(separar[0] == 'santo')
