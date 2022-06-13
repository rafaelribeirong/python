salario = float(input('Digite valor do seu salario: '))
print('CALCULANDO O AUMENTO . . .')
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava {:.2f}, vai ganhar R$ \033[0;30;41m{:.2f}\033[m'.format(salario, novo))