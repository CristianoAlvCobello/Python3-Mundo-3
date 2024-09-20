from random import randint
from time import sleep

qtdJogos = int(input('Quantos jogos você quer sortear? '))

print('')
for jogos in range(1, qtdJogos+1):
    jogo = []
    for numeros in range(0, 6):
        numeroSorteado = randint(1, 60)
        while numeroSorteado in jogo:
            numeroSorteado = randint(1,60)
        jogo.append(numeroSorteado)
    sleep(1)
    print(f'Jogo {jogos}: {sorted(jogo)}')
print('')
print('-='*5, '< BOA SORTE >', '=-'*5)