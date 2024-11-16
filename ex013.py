# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Quanto você recebe de salário? R$'))

aumento = salario * 15 / 100
novo_sal = aumento + salario

print('Com um aumento de 15%, seu novo salário será de {:.2f}'.format(novo_sal))