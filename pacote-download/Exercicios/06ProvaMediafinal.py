#média final
prova1 = float(input('nota da prova 1: '))
prova2 = float(input('nota da prova 2: '))
prova3 = float(input('nota da prova 3: '))
mediafinal = (prova1 + prova2 + prova3)/3
if mediafinal >= 8:
  print('Você está aprovado!')
else:
  print('Você foi reprovado!')
