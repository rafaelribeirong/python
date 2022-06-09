largura = float(input('Qual a largura da sua parede: '))
altura = float(input('Qual a altura da sua parede: '))
print('Dimenssão é {}x{} area para pintar é {}m² \n Você vai gastar o total {}L de tinta'.format(largura, altura, (largura*altura), largura*altura/2))

#exemplo 2 do professor

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimenssão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area /2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))