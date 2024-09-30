from time import sleep

def maior(numeros):
    print('-'*40)
    print('Analisando os valores passados...')
    for numero in numeros:
        sleep(0.5)
        print(numero, end=' ')
    print(f'Foram informados {len(numeros)} valores ao todo')
    if len(numeros) == 0:
        maior = 0
    else:
        for contador in range(0, len(numeros)):
            if contador == 0:
                maior = numeros[0]
            else:
                if maior < numeros[contador]:
                    maior = numeros[contador]
    print(f'O maior valor informado foi {maior}')

maior([2, 9, 4, 5, 7, 1])
maior([4, 7, 0])
maior([1, 2])
maior([6])
maior([])
