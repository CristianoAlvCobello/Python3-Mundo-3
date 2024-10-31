from funções import *
from time import sleep

arquivo = 'dadosEx115.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar pessoas', 'Sair do programa'])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 2:
        lerArquivo(arquivo)
    elif resposta == 3:
        print('Encerrando a execução...')
        break
    else:
        print('\033[31mOpção inválida, tente novamente...\033[m')
    sleep(1)