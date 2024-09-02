numeros = []
while True:

    numero = int(input('Digite um número: '))
    if numero not in numeros[:]:
        numeros.append(numero)
    else:
        print('Número repetido')

    mais = str(input('Quer mais números (s/n)? ')).lower()
    if mais != 's':
        break

print(sorted(numeros))
