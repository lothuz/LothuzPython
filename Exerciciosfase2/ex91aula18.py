from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1':randint(1,6),
        'Jogador2':randint(1,6),
        'Jogador3':randint(1,6),
        'Jogador4':randint(1,6)}
rank = []
print('Valores Sorteados: ')
for k,v in jogo.items():
    print(f'{k} jogou: {v}')
    sleep(1)
print('-=' * 30)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
