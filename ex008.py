# Escreva um programa que leia um valor em metros e o exiba convertido em
# milimetros, centimetros, decimetros, decametros, hectometros e kilometros.

n = float(input('Digite um valor em metros: '))

print('O valor convertido para milimetros é: {:.3f} mm'.format(n * 1000))
print('O valor convertido para centimetros é: {:.3f} cm'.format(n * 100))
print('O valor convertido para decimetros é: {:.3f} dm'.format(n * 10))
print('O valor convertido para decametros é: {:.3f} dam'.format(n / 10))
print('O valor convertido para hectometros é: {:.3f} hm'.format(n / 100))
print('O valor convertido para kilometros é: {:.3f} km'.format(n / 1000))
