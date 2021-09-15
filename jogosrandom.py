import random
lista = []
listamaior =[]
jogos = int(input('Quantos jogos deseja fazer?'))
cont = 0
while cont < jogos:
    if cont <= jogos:
        while True:
            num = random.randint(0,60)
            if num in lista:
                num = random.randint(0,60)
            else:
                lista.append(num)
                if len(lista) ==6:
                    break
        lista.sort()
        listamaior.append(lista[:])
        lista.clear()
        cont += 1
print(listamaior)