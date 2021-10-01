#Escreva um programa qe leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('Digite o valor em metros: '))

km = metros/1000

hm = metros/100

dam = metros/10

dcm = metros * 10

cm= metros * 100

mm = metros * 1000

print('{}m é equivalente \n{}km \n{}hm \n{}dam \n{}dcm \n{}cm \n{}mm' .format(metros, km, hm, dam, dcm, cm, mm))
