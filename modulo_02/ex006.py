peso = float(input("Qual é seu peso? (Kg)"))
altura = float(input("Qual é sua altura? (m)"))
imc = peso / (altura ** 2)
if imc <18.5:
   print("Seu IMC é {:.2f} e você está ABAIXO DO PESO.".format(imc))
elif imc <=25:
   print("Seu IMC é {:.2f} e você está com PESO IDEAL.".format(imc))
elif imc <=30:
   print("Seu IMC é {:.2f} e você está com SOBREPESO.".format(imc))
elif imc <=40:
   print("Seu IMC é {:.2f} e você está com OBESIDADE.".format(imc))
else:
   print("Seu IMC é {:.2f} e você está com OBESIDADE MÓRBIDA.".format(imc))