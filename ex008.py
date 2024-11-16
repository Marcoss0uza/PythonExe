# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Informe o valor em metros: '))
cm = metro * 100
mm = metro * 1000

print('O valor em metros convertido em centímetros é {}cm e em milímetros {}mm'.format(cm, mm))