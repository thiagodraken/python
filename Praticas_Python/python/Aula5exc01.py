'''Conversao de Celsius para Farenheit'''

tc = float(input('Digite a temperatura em Celsius: '))
tf = 1.8 * tc + 32

print('A temperatura {} Celsius em Farenheit {:.2f}'.format(tc,tf))