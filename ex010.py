# Crie um promagrama que leia quanto dinheiro ela tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27

real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = float(real / 5.80)

print('Você pode comprar US${:.2f}'.format(dolar))


