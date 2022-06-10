n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2
print('Asua média foi {:.1f}'.format(n))
if n >=6.0:
    print('Boa nota, PARABÉNS!')
else:
    print('Sua nota foi ruim, ESTUDE!')    