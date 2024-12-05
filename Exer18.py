# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Digite uma data no formato dd/mm/aaaa: ')
dia, mes, ano = data.split('/')

if mes < 1 or mes > 12:
    print('Data inválida.')
else:
    print('Data válida.')
    
if dia < 1 or dia > 31:
    print('Data inválida.')
else:
    print('Data válida.')
    
if ano < 0:
    print('Data inválida.')
else:
    print('Data válida.')
