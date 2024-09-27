from random import randint
from time import sleep
from operator import itemgetter

jogo = {}

print('Valores sorteados:\n')
for contador in range(1, 5):
    jogo[f'jogador {contador}'] = randint(1, 6)

for chave, valor in jogo.items():
    sleep(1)
    print(f'{chave} tirou o número {valor}')

ranking = (sorted(jogo.items(), key=itemgetter(1), reverse=True))

print('\nRanking:\n')
for ranks in ranking:
    sleep(1)
    print(f'{ranks}')
