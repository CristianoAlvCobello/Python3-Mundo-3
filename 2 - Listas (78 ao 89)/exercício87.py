matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
somapares = 0
somacoluna3 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = (int(input(f'Digite o valor da posição [{linha}, {coluna}]: ')))

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz [linha] [coluna] % 2 == 0:
            somapares += matriz[linha] [coluna]
        if coluna == 2:
            somacoluna3 += matriz[linha] [coluna]
        if linha == 1:
            if coluna == 0:
                linha2maior = matriz[linha] [coluna]
            else:
                if matriz[linha] [coluna] > linha2maior:
                    linha2maior = matriz[linha] [coluna]

print('\nA matriz gerada\n')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^1} ]', end='')
    print('\n')

print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somacoluna3}')
print(f'O maior valor da segunda linha é {linha2maior}')
