n = input('Digite algo: ')
print('O tipo primitivo desse valor é?', type(n))
print('Só tem espaços? ', n.isspace())
print('É um numero? ', n.isnumeric())
print('É alfanumerico? ', n.isalpha())
print('Está em maiúsculo? ', n.isupper())
print('Está em minúsculo? ', n.islower())
print('Está capitalizado? ', n.istitle())

