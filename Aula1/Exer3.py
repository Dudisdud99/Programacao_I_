# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

x = input('Digite F para feminino ou M para masculino: ')
if x.upper() == 'F':
    print('F - Feminino')
elif x.upper() == 'M':
    print('M - Masculino')
else:
    print('Sexo inválido.')
