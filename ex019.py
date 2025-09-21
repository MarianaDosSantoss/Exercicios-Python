# Um professor quer sortear um dos seus quatro alunos para a pagar o quadro. Faça um programa que ajude ele, lendo o nome 
# deles e escrevendo o nome do escolhido.

from random import choice 

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
aluno_escolhido = choice(lista)

print('O aluno sorteado para apagar o quadro é {}'.format(aluno_escolhido))
