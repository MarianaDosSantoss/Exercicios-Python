# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar considere USS 1,00 = RS 3,27

n = float(input('Digite a quantidade de dinheiro que você possui: '))
print('Com R${:.2f} você pode comprar US${:.2f}'. format(n, n /3.27 ))