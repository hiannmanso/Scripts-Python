import random
lista =['pedra', 'papel','tesoura']
c = random.choice(lista)

escolha = str(input('Escolha entre pedra, papel e tesoura:'))
from  time import sleep
for contagem in range(0,1):
    sleep(1)

print('Jokenpo...')
for contagem in range(0,3):
    sleep(1)

print('.... ')
print('Voce escolheu {} contra {}'.format(escolha,c))
if escolha == "pedra" and c== "pedra" or escolha =="papel" and c=="papel" or escolha =="tesoura" and c =="tesoura":
    print('Empatou')
elif escolha =="pedra" and c=="tesoura" or escolha =="tesoura" and c =="papel" or escolha =="papel" and c=="pedra":
    print('voce ganhou')
else:
    print('voce perdeu')

