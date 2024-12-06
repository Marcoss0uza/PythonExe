# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite do funcionário: R$'))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

# Novo salário após o aumento
novo_salario = salario + aumento

print('O aumento será de R${:.2f}.'.format(aumento))
print('O novo salário será de R${:.2f}'.format(novo_salario))