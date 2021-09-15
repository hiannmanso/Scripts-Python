import random
import time
from operator import itemgetter
jogo = {'jogador1': random.randint(0,6),
        'jogador2': random.randint(0,6),
        'jogador3': random.randint(0,6),
        'jogador4': random.randint(0,6)
        }
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
rank = {}
rank = sorted(jogo.items(),key=itemgetter(1),reverse=True)
for pos, v in enumerate(rank):
    print(f'{pos+1}º lugar, o {v[0]} com {v[1]}')