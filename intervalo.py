import time


def contador(x, y, z):
    print(f'Contagem de {x} até {y} de {z} em {z}')
    if y > x and z < 0 or x > y and z > 0:
        z = - (z)
        for val in range(x, y+1, z):
            print(f'{val} ',end='')
            time.sleep(0.5)
        print('Fim')
    if z == 0:
        z = 1
        for val in range(x, y+1, z):
            print(f'{val} ',end='')
            time.sleep(0.5)
        print('Fim')
    else:
        for val in range(x,y+1,z):
            print(f'{val} ', end='')
            time.sleep(0.5)
        print('Fim')



x = int(input('Início: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contador(x,y,z)