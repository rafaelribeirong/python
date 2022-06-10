letra = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {}'.format(letra.count('A')))
print('A primeira letra A aparece na posição {} '.format(letra.find('A')+1))
print('A ultima letra A aparece na posição {} '.format(letra.rfind('A')))
