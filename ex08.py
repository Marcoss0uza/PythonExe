# Faça um programa que leia um valor em metros e converta em km, hm, dam, dm, cm  e mm.

medida = float(input('Uma distância em metros:'))

km = float(medida/1000)
hm = float (medida/100)
dam = float(medida/10)
dm = float(medida*10)
cm = float(medida*100)
mm = float(medida*1000)

print('A medida em {}m convertida para quilômetro é {}km.'.format(medida, km))
print('A medida em {}m convertida para hectômetro é {}hm.'.format(medida, hm))
print('A medida em {}m convertida para  decâmetro é {}dam.'.format(medida, dam))
print('A medida em {}m convertida para decímetro é {:.1f}dm.'.format(medida, dm))
print('A medida em {}m convertida para centímetro é {:.1f}cm.'.format(medida, cm))
print('A medida em {}m convertida para melímetro é {:.1f}mm.'.format(medida, mm))

