viagem = float(input('Qual a distancia da sua viagem? '))
print('Você está para começar uma viagem de {:.1f} Km'.format(viagem))
if viagem <= 200:
    km = viagem*(0.50)
else:
    km = viagem*(0.45)
print('Sua viagem vai custar R${:.2f}'.format(km))




