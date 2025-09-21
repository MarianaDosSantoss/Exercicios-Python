# Faça um programa que leia um ângulo qualquer e mostre na tela o valor  do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno do ângulo {:.2f} é {:.2f}'.format(angulo, seno))
print('O cosseno do ângulo {:.2f} é {:.2f}'.format(angulo, cosseno))
print('A tangente do ângulo {:.2f} é {:.2f}'.format(angulo, tangente))