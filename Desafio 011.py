#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Digite a altura da parede: '))

largura = float(input('Digite a largura da parede: '))

parede = largura*altura

tinta = parede/2

print('A parede tem {}m², para essa medida será necessário {}L de tinta' .format(parede, tinta))
