# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 
# até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Digite a distância da sua viagem em km: '))

if distancia < 200:
   preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O preço da passagem para a sua viagem de {:.1f}Km é R${:.2f}'.format(distancia, preco))

# Outra forma de resolver

preco = distancia * 0.50 if distancia < 200 else distancia * 0.45