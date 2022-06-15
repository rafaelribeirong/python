from datetime import date
print("\033[1;30;41m A CONFEDERAÇÃO NACIAL DE NATAÇÃO, AGRADECE SEU INTERESSE!\033[m")
atual = date.today().year
nascimento = int(input("Por favor, informe ano de nascimento: "))
idade = atual - nascimento
print("O atleta tem {}".format(idade))
if idade <= 9:
    print("Por favor se cadastrar na modalidade MIRIM!")
elif idade <= 14:
    print("Por favor se cadastrar na modalidade INFANTIL!")
elif idade <= 19:
    print("Por favor se cadastrar na modalidade JÚNIOR!")
elif idade <= 25:
    print("Por favor se cadastrar na modalidade SÊNIOR!")
else:
    print("Por favor se cadastrar na modalidade MASTER!")