# Escreva um programa que converte uma temperatura digitada em celsius e converta para fahrenheit.

celsius= float(input('Digite uma temperatura em Celsius: '))

fahrenheit = (celsius * 1.8) + 32

print('{:.1f} Celsius equivalem a {:.1f} Farenhit'.format(celsius, fahrenheit))