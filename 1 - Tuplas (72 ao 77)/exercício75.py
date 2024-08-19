num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))
num4 = int(input('Digite o número 4: '))

numeros = (num1, num2, num3, num4)

print(f'\nO número nove aparece: {numeros.count(9)}')

if 3 not in numeros:
     print('Não aparece numero três em nenhuma posição')
else:
    print(f'O número três apareceu na posição: {numeros.index(3)+1}')

print(f'Os números pares que apareceram foram: ', end='')
for pares in numeros:
    if pares%2 == 0:
          print(pares, end=' ')
