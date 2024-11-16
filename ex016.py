# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
oposto = float(input('Informe qual é o cateto oposto: '))
adja = float(input('Informe qual o cateto adjacente: '))
hipo = hypot(oposto, adja)

print('De acordo com o comprimento do cateto oposto {} e do adjacente {}, o comprimento da hipotenusa '
      'é {:.2f}'.format(oposto, adja, hipo))