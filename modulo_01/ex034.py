carro = float(input('Qual velocidade do seu carro: '))
print('PROCESSANDO . . .')
if carro > 80:
    print('MULTADO, você excedeu o limite de 80Km/h')
    km = (carro-80)*7
    print('Você deve pagar uma multa de R$ {:.2f}'.format(km))
print('Tenha um bom dia, dirija com cuidado!')    





  