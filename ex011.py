# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura 

print('A área da sua parede é {:.3f} metros quadrados'.format(area))
print('A quantidade de tinta necessária para pinta-la é de {:.3f} litros'.format(area / 2))