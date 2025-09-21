# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex:
# Ana Maria de Souza
# primeiro = Ana
# segundo = Souza

nome = str(input('Digite o nome completo de uma pessoa: ')).strip()

nome_divido = nome.split()
tam = len(nome_divido)

print('Primeiro = {}'.format(nome_divido[0]))
print('Último = {}'.format(nome_divido[tam-1]))