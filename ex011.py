# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e
# a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))

area = altura * largura
tinta = area / 2

print('Para pintar a área de {} é necessário {} litros de tinta'.format(area, tinta))




