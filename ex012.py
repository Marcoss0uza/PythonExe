# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o preço do produto? R$ '))
desconto = preço * 5 / 100
a_pagar = preço - desconto

print('Seu produto com o valor R${:.2f} com 5% de desconto ficou por R${:.2f}'.format(preço, a_pagar ))