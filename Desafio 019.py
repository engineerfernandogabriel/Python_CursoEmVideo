#Um progessor quer sortear um ds seus quatro alunos para apagar o quadro. Faça um programa que ajude ele
#lendo o nome deles e escrevendo o nome do escolhido

import random

nome1 = str(input('Digite o nome do primeiro aluno: '))

nome2 = str(input('Digite o nome do segundo aluno: '))

nome3 = str(input('Digite o nome do terceiro aluno: '))

nome4 = str(input('Digite o nome do último aluno: '))

lista = [nome1, nome2, nome3, nome4]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}' .format(escolhido))
