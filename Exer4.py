# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

x = input('Digite uma letra: ')

if x in 'aeiou':
    print(f'{x} é uma vogal.')
else:
    print(f'{x} é uma consoante.')
