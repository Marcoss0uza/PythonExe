# Faça um programa que leia um número inteiro e mostre na tele o seu sucessor e seu antecessor.

num = int(input('Digite um número: '))
suc = num + 1
ant = num - 1

print('Seu sucessor é {} e seu antecessor é {}'.format(suc, ant))