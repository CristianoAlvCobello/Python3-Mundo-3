from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista', end=' ')
    for numero in range(1,6):
        lista.append(randint(0, 10))
    for numero in lista:
        sleep(1)
        print(numero, end=' ')
    print('Pronto!')

def somaPar(lista):
    pares = 0
    print('Somando os valores pares de', end='')
    for numero in lista:
        if numero%2 == 0:
            sleep(1)
            print(f' {numero}', end='')
            pares += 1
    print(f', temos {pares} pares')

minhalista = []

sorteia(minhalista)
somaPar(minhalista)
