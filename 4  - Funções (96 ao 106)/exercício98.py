from time import sleep

def contador(inicio, fim, passo):
    print('-'*40)
    if -passo == True:
        if passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo*-1} em {passo*-1}')
        for contador in range(inicio, fim-1, passo):
            print(f'{contador}', end=' ')
            sleep(0.5)
    elif inicio > fim:
        if passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for contador in range(inicio, fim-1, passo*-1):
            print(f'{contador}', end=' ')
            sleep(0.5)
    else:
        if passo == 0:
            passo = 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for contador in range(inicio, fim+1, passo):
            print(f'{contador}', end=' ')
            sleep(0.5)
    print('FIM')

contador(1, 10, 1)

contador(10, 0, 2)

print('\nAgora é sua vez de personalizar a contagem')
inicio = int(input('\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
