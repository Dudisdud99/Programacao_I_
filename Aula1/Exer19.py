# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

while True:
    x = int(input('Digite um número inteiro menor que 1000: '))
    if x <= 1000 or x >= 0:
        break

cent = x//100
dez = x%100//10
uni = x%10

print(f'{x} = {cent} centena, {dez} dezenas e {uni} unidades')