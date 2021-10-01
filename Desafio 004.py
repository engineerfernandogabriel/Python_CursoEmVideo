p1 = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(p1))

print('Só tem espaços ? ', p1.isspace())

print('É um número ?', p1.isnumeric())

print('É alfabético ?', p1.isalpha())

print('É alfanumérico ?', p1.isalnum())

print('Está em maiscúla ?', p1.isupper())

print('Está em minúscula ?', p1.islower())

print('Está capitalizada ?', p1.istitle())
