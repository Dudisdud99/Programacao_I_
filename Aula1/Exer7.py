# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    if n2 < n3:
        menor = n2
    maior = n1
elif n2 > n1 and n2 > n3:
    if n1 < n3:
        menor = n1
    maior = n2
else:
    if n1 < n2:
        menor = n1
    maior = n3
    
print(f'O maior número é {maior} e o menor número é {menor}.')