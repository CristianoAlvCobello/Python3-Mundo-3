matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = (int(input(f'Digite o valor da posição [{linha}, {coluna}]: ')))

print('\nA matriz gerada\n')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^1} ]', end='')
    print('\n')
