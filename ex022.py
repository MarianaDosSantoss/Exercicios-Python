# Crie um programa que leia o nome completo e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas minúsculas;
# Quantas letras ao todo (sem considerar espaços);
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

print('Analisando seu nome: ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))

# Outra forma de resolver: 
print('Seu nome tem {} letras'.format(len(nome.strip()) - nome.count(' ')))
