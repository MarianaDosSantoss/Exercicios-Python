# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a nome 'SANTO'

cidade = str(input('Digite o nome de uma cidade: '))

print('Esta cidade começa com o nome Santo? ')
print('santo' in cidade.strip().lower().split()[0])

# Outra forma de resolver:

cid = str(input('Digite o nome de uma cidade: ')).strip()

print('Esta cidade começa com o nome Santo? ')
print(cid[:5].upper() == 'SANTO')