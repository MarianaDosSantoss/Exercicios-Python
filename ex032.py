#  Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano é bissexto.')   
        else:
            print('O ano não é um ano bissexto.')
    else:
        print('O ano é bissexto.')
else:
    print('O ano não é um ano bissexto.')

# Outra forma de resolver

print('Coloque 0 para analisar o ano atual: ')

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto.')   
else:
    print('O ano não é um ano bissexto.')