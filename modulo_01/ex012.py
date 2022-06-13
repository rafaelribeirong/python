dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Você tem R$ {:.2f} = U$$ {:.2f} '.format(dinheiro, dinheiro/3.27))
print('-' *20)



#EXEMPLO 2

real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar U$${:.2f}'.format(real, dolar))