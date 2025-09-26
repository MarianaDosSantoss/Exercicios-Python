# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o segundo número: '))

menor = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O número {:.2f} é o maior.'.format(maior))
print('O número {:.2f} é o menor.'.format(menor))