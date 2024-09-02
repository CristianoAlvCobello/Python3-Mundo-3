numeros = list()

for contador in range(1, 6):
    n = int(input('Digite um número: '))
    
    if contador == 1:
        numeros.append(n)
        print('Adicionado na lista')
        
    else:
        for posicao in range(0, len(numeros)):

            if numeros[-1] < n:
                numeros.append(n)
                print('Adicionado no fim da lista')
                break

            elif numeros[posicao] > n:
                numeros.insert(posicao, n)
                print(f'Adicionado na posição {posicao}')
                break

print(f'\n{numeros}')

#Resposta do professor
#if contador == 1 or numeros[-1] < n:
#numeros.append(n)