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
