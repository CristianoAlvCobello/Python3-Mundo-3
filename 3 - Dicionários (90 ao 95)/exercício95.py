from time import sleep

jogadores = []
gols = []
total = 0
resposta = 's'

while resposta == 's':

    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for partida in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {partida}: ')))
        total += gols[partida-1]

    jogador['gols'] = gols
    jogador['total'] = total
    jogadores.append(jogador.copy())

    gols = []
    total = 0

    resposta = str(input('Quer continuar(S/N)? '))
    print('-'*50)

contador = 0
for individuo in jogadores:
    contador += 1
    print(f'{contador:<4}', end='')
    sleep(1)
    print(f'{individuo["nome"]:<20}', end='') 
    sleep(1)
    print(f'{(str (individuo["gols"])):<25}', end='') 
    sleep(1)
    print(f'{individuo["total"]:<10}')

while True:
    print('-'*50)
    jogador = int(input('Mostrar dados de qual jogador(999 para)? '))
    if jogador == 999:
        print('FIM DA EXECUSÃO')
        break
    elif jogador > len(jogadores) or jogador <= 0:
        print(f'ERRO! Não existe jogador com o número {jogador}! Tente novamente')
        continue
    gols = jogadores[jogador-1] ['gols']
    
    print(f'\nLEVANTAMENTO DO JOGADOR {jogadores[jogador-1] ['nome']}')
    for posicao, gol in enumerate(gols):
        sleep(1)
        print(f'No jogo {posicao+1} fez {gol}')
