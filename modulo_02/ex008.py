from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Teseoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é sua jogada? '))
print('JOO')
sleep(1)
print('KENN')
sleep(1)
print('POO!!!')
sleep(1)
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
   if jogador == 0:
      print('EMPATE')
   elif jogador == 1:
      print('JOGADOR GANHOU')
   elif jogador == 2:
      print('JOGADOR PERDE')
   else:
      print('JOGADA INVÁLIDA!')
elif computador ==1:
   if jogador == 0:
     print('COMPUTADOR VENCE')
   elif jogador == 1:
      print('EMPATE')
   elif jogador == 2:
      print('JOGADOR VENCE')
   else:
      print('JOGADA INVALIDA!')
elif computador == 2:
   if jogador == 0:
      print('JOGADOR VENCE')
   elif jogador == 1:
      print('COMPUTADOR VENCE!')
   elif jogador == 2:
      print('EMPATE!')
   else:
      print('JOGADA INVALIDA!')