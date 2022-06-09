#QUEBRANDO UM NUMERO
#EXEMPLO 1 IMPORTANDO O MATH COMPLETO

import math
v = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira {}'.format(v, math.trunc(v)))

#EXEMPLO 2 IMPORTANDO APENAS O QUE QUERO DO MATH


from math import trunc
v = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira {}'.format(v, trunc(v)))

#EXEMPLO 3

v = float(input('Digite um valor: '))
print('O valor digitalizado foi {} e a sua porção inteira é {}'.format(v, int(v)))

