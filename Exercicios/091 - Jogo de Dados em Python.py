from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador1': randint(1,6),'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),'Jogador4': randint(1,6)}

print('Valores sorteados:')
ranking = dict()
for i,k in jogo.items():
    print('{} tirou {} no dado.'.format(i,k))
    sleep(1)
ranking = sorted(jogo.items(),key = itemgetter(1), reverse= True)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print('   {} lugar: {} com {}.'.format(i+1,v[0], v[1]))
    sleep(1)

