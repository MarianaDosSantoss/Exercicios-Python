# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e 
# mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

h = math.sqrt((math.pow(cateto_oposto, 2)) + (math.pow(cateto_adjacente, 2)))
print('O comprimento da hipotenusa é {:.4}'.format(h))

# Outra forma de resolver: 

hi = math.hypot(cateto_oposto, cateto_adjacente)
print('O comprimento da hipotenusa é {:.4}'.format(hi))



