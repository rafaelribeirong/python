from random import randint
computador = randint(0, 5) #faz o pc 'pensar' aleatorio entre 0 e 5
print('--=--' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar . . .')
print('--=--' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
if jogador == computador:
    print('Parabéns você me venceu!')
else:
    print('Perdeu!, eu pensei no {} e não no {}'.format(computador, jogador))

