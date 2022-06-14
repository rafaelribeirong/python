casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu sálario: '))
anos = int(input('Quantos anos você pagará a casa?'))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print (' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print ('Empréstimo pode ser CONCEDIDO!')
else:
    print ('Empréstimo NEGADO!')