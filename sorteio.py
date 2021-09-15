import random

lista = []
def sorteio():
    lista.append(random.randint(0,20))
    lista.append(random.randint(0, 20))
    lista.append(random.randint(0, 20))
    lista.append(random.randint(0, 20))
    lista.append(random.randint(0, 20))
    print(lista)
def somaPar():
    soma = 0
    for pos, val in enumerate(lista):
        if lista[pos] % 2 == 0:
            soma += val
    print(soma)

sorteio()
somaPar()