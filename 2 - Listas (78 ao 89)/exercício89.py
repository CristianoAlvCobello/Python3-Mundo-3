from time import sleep

galera = []
resposta = 's'

while resposta == 's':
    aluno = ['nome', []]
    aluno[0] = str(input('Nome: '))
    aluno[1].append(float(input('Nota 1: ')))
    aluno[1].append(float(input('Nota 2: ')))
    galera.append(aluno)
    resposta = str(input('\nQuer continuar(s/n)? ')).lower()
    print('')

print(f'\n{"Nº":<4}{"Nome":<15}{"Média":>4}\n')
for contador in range(0, len(galera)):
    media = (galera[contador] [1] [0] + galera[contador] [1] [1])/2
    print(f'{contador:<4}{galera[contador] [0]:<15}{media}')

while True:
    aluno = int(input('\nMostrar nota do aluno(999 interrompe)? '))
    if aluno < len(galera):
        if aluno != 999:
            print(f'\nAs notas de {galera[aluno] [0]} são {galera[aluno] [1] [0:]}')
    else:
        print('\nFinalizando...')
        sleep(1)
        print('<<< Volte sempre >>>')
        break
