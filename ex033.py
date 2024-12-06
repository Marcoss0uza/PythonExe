# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#Determina o maior número
maior = max(n1, n2, n3)

#Determina o menor número
menor = min(n1, n2, n3)

print('O número maior é o {}.'.format(maior))
print('O número menor é {}.'.format(menor))

