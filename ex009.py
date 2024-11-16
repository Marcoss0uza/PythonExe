# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

tabuada = int(input('Qual tabuada você deseja saber: '))

for count in range(11):
    print(f'{tabuada} x {count} = {(tabuada * count)}')
