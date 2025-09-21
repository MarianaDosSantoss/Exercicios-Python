# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input('Digite o nome de uma pessoa: ')).strip()

print('O nome dessa pessoa tem Silva?')
print('silva' in nome.lower())