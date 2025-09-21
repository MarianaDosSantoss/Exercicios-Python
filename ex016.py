# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

from math import trunc

n = float(input("Digite um número Real: "))

print('O número {} tem a parte inteira igual a {}'.format(n, trunc(n)))

# Outra forma de resolver:

print('O número {} tem a parte inteira igual a {}'.format(n, int(n)))