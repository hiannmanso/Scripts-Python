def metade(x,form=False):
    met = x/2
    return met if form is False else format(met)


def dobro(x,form=False):
    dob = x*2
    return dob if form is False else format(dob)


def aumento(x,y,form=False):
    up = x+(x*(y/100))
    return up if form is False else format(up)


def diminuir(x,z,form=False):
    down= x-(x*(z/100))
    return down if form is False else format(down)


def format(x=0,moeda='R$'):
    return f'{moeda}{x:>8.2f}'.replace('.',',')


def resumo(x, y, z):
    print(metade(x, True))
    print(dobro(x, True))
    print(aumento(x, y, True))
    print(diminuir(x, z, True))