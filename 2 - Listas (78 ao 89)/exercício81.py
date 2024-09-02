numeros = list()

while True:
    numeros.append(int(input('Digite um número: ')))

    mais = str(input('Quer mais? ')).lower()

    if mais != 's':
        break

print(f'\nForam digitados {len(numeros)} números')
print(f'Os valores em ordem decrescente {sorted(numeros, reverse=True)}')

if 5 in numeros:
    print('A lista possui o número 5')
else:
    print('A lista não possui o número 5')
