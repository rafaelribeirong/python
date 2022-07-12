num = int(input('Digite o número da tabuada que deseja ver: '))
for c in range(1, 11):
   print('{} x {:2} = {}'.format(num, c, num*c))