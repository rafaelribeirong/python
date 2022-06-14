m1 = float(input("Qual sua primeira nota: "))
m2 = float(input("Qual sua segunda nota: "))
nota = (m1 + m2) / 2
if nota < 5.0:
    print("Sua média foi {}, REPROVADO.".format(nota))
elif nota >= 7.0:
    print("Sua média foi {}, APROVADO.".format(nota))
else:
    print("Sua média foi {}, RECUPERAÇÃO".format(nota))
