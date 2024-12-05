# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

x = int(input('Digite um número: '))

if x == 1:
    print('1 - Domingo')
elif x == 2:
    print('2 - Segunda')
elif x == 3:
    print('3 - Terça')
elif x == 4:
    print('4 - Quarta')
elif x == 5:
    print('5 - Quinta')
elif x == 6:
    print('6 - Sexta')
elif x == 7:
    print('7 - Sábado')
else:
    print('Valor inválido.')