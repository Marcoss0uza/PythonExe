# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_1 = float(input('Qual a primeira nota: '))
nota_2 = float(input('Qual a segunda nota: '))
media = float(nota_1 + nota_2)/2

print('Sua nota média é {:.1f}'.format(media))

