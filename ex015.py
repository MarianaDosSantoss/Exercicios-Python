# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço
# a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

quilometragem = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quatidade de dias pelas quais alugou o carro: '))

valor = (quilometragem * 0.15) + (dias * 60)

print('O valor pago pelos dias e pela quilometragem utilizada é de R${:.2f}'.format(valor))