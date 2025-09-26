# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido 
# pelo computador.

# O programa deverá escever na tela se o usuário venceu ou perdeu.

import random
from time import sleep 

lista = [0, 1, 2, 3, 4, 5]
numero = random.choice(lista)

print('--' * 40)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('--' * 40)
numero_usuario = int(input('Em que número pensei? '))

print('PROCESSANDO...')
sleep(2)

if numero_usuario == numero:
    print('Correto! Este foi o número escolhido pelo computador.')
else:
    print('Incorreto, tente novamente.')

# Outra forma de fazer 
    # numero = random.randint(0,5)