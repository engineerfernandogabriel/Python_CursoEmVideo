#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite o seu nome completo: ')).strip()

min = nome.lower()

procsilva = 'silva' in min

print('O seu nome tem "Silva" ? {}' .format(procsilva))



#nome = str(input('Digite o seu nome completo: ')).strip()

#nomemin = nome.lower()

#silva = nomemin.find('silva')

#print('O seu nome tem "Silva":' )

#print(silva > -1)
