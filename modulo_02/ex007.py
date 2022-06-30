preço = float(input("Qual valor do seu produto: R$"))
print ('''
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO
''')
opção = int(input("Qual opção? "))
if opção == 1:
   total = preço - (preço * 10 / 100)
elif opção == 2:
   total = preço - (preço * 5 / 100)
elif opção == 3:
   total = preço
   parcela = preço / 2
   print("Sua compra será dividida em 2x de {:.2f}".format(parcela))
elif opção == 4:
   total = preço + (preço * 20 / 100)
   dividida = int(input("Em quantas VEZES deseja parcelar:"))
   parcela = total / dividida
   print("Sua compra será dividida em {}x a parcela vai custar {:.2f} e terá um total de {:.2f}".format(dividida, parcela, total))
else:
   total = 0
   print("Opção invalida de pagamento tente novamente!")
print("Sua compra tem o valor de R${:.2f} e vai custar {:.2f}".format(preço, total))