numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Digite um número: ')))

    mais = str(input('Quer mais(s/n)? ')).lower()
    if mais != 's':
        break

for analise in numeros:
    if analise%2 == 0:
        pares.append(analise)
    else:
        impares.append(analise)

print(f'\nLista principal: {numeros}')
print(f'Lista com os pares: {pares}')
print(f'Lista com ímpares: {impares}')
