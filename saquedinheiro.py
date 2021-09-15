cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
print('=' * 30)
print('{:^30}'.format('SAQUE DE DINHEIRO'))
print('=' * 30)
valor = int(input('Qual valor deseja sacar? '))
while True:
    if valor >=50:
        cont50 +=1
        valor -= 50
    if valor < 50 and valor > 19:
        cont20 +=1
        valor -=20
    if valor <=19 and valor >9:
        cont10 +=1
        valor -=10
    if valor <=9 and valor >0:
        cont1 +=1
        valor -=1
    if valor ==0:
        break
print("""
São ao total {} notas de 50
{} Notas de 20
{} Notas de 10
{} Notas de 1""".format(cont50,cont20,cont10,cont1))
