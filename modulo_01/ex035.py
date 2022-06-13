numero = int(input( 'Me diga um número qualquer: '))
print('Vou adivinhar se é IMPAR ou PAR.')
print('DEIXA EU PENSAR . . .')
resultado = numero % 2
if resultado == 0:
    print('Você escolheu um número PAR!')
else:
    print('Você escolheu um número IMPAR!')