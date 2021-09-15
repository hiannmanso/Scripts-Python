import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]
ran = random.choice(lista)
print('Acabei de pensar em um número entre o e 10.')
print('Será que você consegue adivinhar qual foi?')
pal = ''
cont = 0
while pal != ran:
    pal = int(input('Qual é seu palpite?'))
    cont +=1
    if pal < ran:
        print('Mais.. tente mais uma vez.')
    if pal > ran:
        print('Menos... tente mais uma vez')
print('Parabens! voce acertou com {} tentativas.'.format(cont))
