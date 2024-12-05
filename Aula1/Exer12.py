# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

valor = float(input('Digite o valor da hora trabalhada: '))
horas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor * horas
fgts = salario_bruto * (11 / 100)
sindicato = salario_bruto * (3 / 100)

if salario_bruto <= 900:
    pass
elif salario_bruto <= 1500:
    ir = 5
elif salario_bruto <= 2500:
    ir = 10
else:
    ir = 20
    
salario_liquido = salario_bruto - (salario_bruto * (ir / 100)) - sindicato - fgts

print(f'Salário Bruto: ({valor} * {horas}) : R$ {salario_bruto:.2f}')
print(f'(-) IR ({ir}%): R$ {salario_bruto * (ir / 100):.2f}')
print(f'(-) Sindicato (3%): R$ {sindicato:.2f}')
print(f'FGTS (11%): R$ {fgts:.2f}')
print(f'Total de descontos: R$ {salario_bruto * (ir / 100) + sindicato + fgts}')
print(f'Salário Líquido: R$ {salario_liquido:.2f}')