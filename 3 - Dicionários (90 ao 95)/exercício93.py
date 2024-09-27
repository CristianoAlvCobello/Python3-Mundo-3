jogador = {}
gols = []
total = 0

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for partida in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {partida}: ')))
    total += gols[partida-1]

jogador['gols'] = gols
jogador['total'] = total

print('-='*30)
print(jogador)

print('-='*30)
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas}')
for partida in range(0, partidas):
    print(f'=> Na partida {partida+1}, fez {jogador['gols'] [partida]}')
print(f'Foi um total de {jogador["total"]} gols')
