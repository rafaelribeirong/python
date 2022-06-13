p = float(input('Quanto custa o produto: R$'))
d = p - (p * 5 / 100)
print('O produto custa {:.2f} com 5% de desconto custará {:.2f}'.format(p, d))