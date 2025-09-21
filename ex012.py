# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n = float(input('Digite o preço de um produto: '))

print('O novo preço ao aplicar 5% de desconto é: R${:.2f}'.format( n * 0.95))
