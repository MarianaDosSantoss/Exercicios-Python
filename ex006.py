# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = float(input('Digite um número: '))
print('O dobro do número {:.2f} é {:.2f}'.format(n, n * 2))
print('O triplo do número {:.2f} é {:.2f}'.format(n, n * 3))
print('A raiz quadrada do número {:.2f} é {:.2f}'. format(n, n ** (1/2)))