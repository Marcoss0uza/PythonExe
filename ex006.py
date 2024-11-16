# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))

dob = num * 2
trip = num * 3
raiz = num ** (1/2)

print('O dobro do valor é {}, o triplo do valor é {} e a raiz {:.2f}'.format(dob, trip, raiz))