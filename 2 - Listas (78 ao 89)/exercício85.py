pares = []
impares = []
lista = [pares, impares]

for contador in range(1, 8):
    numero = int(input('Digite um número: '))
    if numero%2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

print(f'\nOs valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')
