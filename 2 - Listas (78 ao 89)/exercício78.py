numeros = []
posicaomaior = []
posicaomenor = []

for contador in range(1, 6):
    numeros.append(int(input('Digite um número: ')))

for contagem in range(0, len(numeros)):
    if contagem == 0:
        maior = numeros[contagem]
        menor = numeros[contagem]
    else:
        if maior < numeros[contagem]:
            maior = numeros[contagem]
        elif menor > numeros[contagem]:
            menor = numeros[contagem]

for posicao in range(0, len(numeros)):
    if numeros[posicao] == maior:
        posicaomaior.append(posicao)
    if numeros[posicao] == menor:
        posicaomenor.append(posicao)

print(f'\nO Maior valor digitado foi {maior} nas posições{posicaomaior}')
print(f'\nO Menor valor digitado foi {menor} nas posições{posicaomenor}')
