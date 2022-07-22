#Exercício - Repetições
print('Tabuada')
print('-'*10)
mult = 0

passo = range(1,5+1)
for i in passo:
  n = int(input('Digite um valor: '))
  mult = mult+n
print('O resultado final é de: {}'.format(mult))
