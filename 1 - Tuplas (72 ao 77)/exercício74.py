from random import randint

contador = 0

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
 
for analise in numeros:
    contador += 1
    if contador == 1:
        maior = analise
        menor = analise
    else:
        if maior < analise:
            maior = analise
        if menor > analise:
            menor = analise

print(f'\nOs números sorteador foram: {numeros}')
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')

#Resposta do professor
#{max(numeros)}, {min(numeros)}, função para puxar o maior e o menor número da tupla 
        