print('~'*30)
f='Jogo da FORCA!'
print(f'{f:^30}')
print('~'*30)
# Tema
titulo = str(input('Escolha um tema pra forca:'))
print(f'TEMA ~>{titulo}')
# palavra
palavra = str(input('Escolha uma palavra ou expressão:')).lower()
palavralista= palavra[:]
lista = []
erradas =[]
# cria uma lista com os caracteres de 'palavra'
for pos, val in enumerate(palavra):
    lista.append(val)
# "blinda"a palavra
# lista não contem os caracteres.
for pos, val in enumerate(lista):
    if lista[pos] != ' ':
       lista[pos] ='_'
    else:
        lista[pos] =' '
print(''.join(lista))
cont =3
tent = 0
# esolhendo uma letra 'letra'
while True:
    letra = str(input('Escolha uma letra')).lower().split()[0]
    tent += 1
    # add letra if letra in palavra
    for pos, val in enumerate(palavralista):
        if palavralista[pos] == letra:
            lista[pos] =letra
    if letra not in palavra:

        print(f'Errou!cuidado, você só tem mais {cont} tentativas!')
        erradas.append(letra)

        cont -= 1
    if cont < 0:
        print('Suas tentativas acabaram! você perdeu!')
        break
    if '_' not in lista :
        print(''.join(lista))
        print(f'Voce ganhou com {tent} tentativas! parabens!')

        break
    print(f'Voce ja errou ~>', end='')
    print(''.join(erradas), end=' ')
    print()
    print(''.join(lista))