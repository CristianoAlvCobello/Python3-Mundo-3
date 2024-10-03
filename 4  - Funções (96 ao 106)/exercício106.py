from time import sleep

def escreva(mensagem, numCor=''):
    linha = len(mensagem)+4
    cor = str(f'\033[{str(numCor)}m')
    fechaCor = str(f'\033[m')
    print('-'*linha)
    print(cor,end='')
    print(f'  {mensagem}  ', end='')
    print(fechaCor)
    print('-'*linha)

resposta = ''
while resposta != 'fim':
    escreva('SISTEMA DE AJUDA PyHELP', 32)
    resposta = str(input('Função ou biblioteca > ')).lower()
    if resposta == 'fim':
        sleep(1)
        escreva('ATE LOGO', 31)
        break
    escreva(f'Acessando o manual do comando {resposta}', 34)
    sleep(1)
    help(resposta)
