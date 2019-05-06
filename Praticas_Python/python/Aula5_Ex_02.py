
"Leitura do salario"
salario = float(input('Digite o salario atual: '))

if salario<=280:
   valorAumento = salario * 0.2
   salarioAntigo = salario
   salario = salario + valorAumento
   porcentual = 20


elif salario<=700:
   valorAumento = salario * 0.15
   salarioAntigo = salario
   salario = salario + valorAumento
   porcentual = 15


elif salario<=1500:
   valorAumento = salario * 0.1
   salarioAntigo = salario
   salario = salario + valorAumento
   porcentual = 10

else:
   valorAumento = salario * 0.05
   salarioAntigo = salario
   salario = salario + valorAumento
   porcentual = 05


'''Exibicao apos o aumento'''
print('Salario antes do reajuste {} '.format(salarioAntigo))
print('Porcentual aplicado {}%'.format(porcentual))
print('Valor do aumento {:.2f}'.format(valorAumento))
print('Novo salario R${:.2f}'.format(salario))

