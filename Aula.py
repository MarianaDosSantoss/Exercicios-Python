import math 
import random
import emoji

# ou
# from math import sqrt
# raiz = sqrt(num)

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz)))

num = random.random()
num = random.randint(1, 10)

print(emoji.emojize("Python is fun :red_heart:"))

# Manipulando cadeias de texto

# fatiamento
# frase[9] -> Só o caracter 
# frase[9:12] -> frase de 9 até 12
# pega sempre um a menos no final, para de contar no 12 mas não pega o 12
# frase [9:21:2]
# frase [onde começa, até onde vai -1, pulando de 2 em dois]
#  frase [:5]
# omitindo começa de 0
# frase[15:] -> mesmo raciocinio
# frase[9::3] 
# começa do nove, vai até o final, pulando de 3 em 3

# análise
# len(frase) -> comprimento da frase
# frase.count('o') -> quantos o aparece na string
# frase.count('o', 0, 13) 
# frase.find('deo') -> diz onde começa essa letra dentro da string
# frase.find('dwqw') -> quando n exite retorna -1
# 'Curso' in frase -> tem curso na frase 


#transformação
# frase.replace('python', 'android') -> substitui o python 
# frase.upper() maiscula
# frase.lower() minusculas
# frase.capitalaze() -> todos os caracteres para minusculas
# e só o primerio caracter fica em maiuscula
#frase.title() -> analisa quantas palavras tem e faz o captalaze
# frase.strip() -> remove espacos inuteis, final e inicio
# frase.rstrip() -> remove só o lado direito 
# frase.lstrip() -> remove só o lado esquerdo

#divisão
# frase.split() -> 'estudar'
# divisão considerando espacos, cria uma divisão nos espacços
# as palavras são colocadas em outras cadeias de caracteres

#junção
#'-'.join(frase) 

frase = 'curso em video python'
print(frase[1:15:2])
frase2 = frase.replace('python', 'Android')
print(frase)
# difirente de 
print(frase2)
print(frase.lower().find('video'))

print("""Texto longo daskdmalsdmaskdmalsd
skdmalskdmalsmdlakdm
alskdmlakmsdlkamsdlkams
alsmdkalskmdlaksmdlkas""")

dividido = frase.split()
print(dividido[0]) 
print(dividido[2][3])
# pedir para o chat dar outras mais usadas

# ------------------------------------------------

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <=3 else 'Carro velho')

nome = str(input('qual o seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem')
print('bom dia gustavo{}'.format(nome))