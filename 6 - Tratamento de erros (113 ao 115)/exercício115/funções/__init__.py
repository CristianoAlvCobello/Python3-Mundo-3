def linha(tamanho=42):
    return '-' * tamanho

def cabeçalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def leiaInt(texto):
    leitura = ''
    leitura = str(input(f'{texto}'))  
    if leitura.isnumeric() == False:
        return leitura
    else:
        return int(leitura)

def menu(lista):
    cabeçalho('MENU DO SISTEMA')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    print(linha())
    opção = leiaInt('Sua Opção: ')
    return opção

#Parte 2

def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Aquivo "{arquivo}" criado com sucesso')

def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos')
    finally:
        a.close()
        
def cadastrar(arquivo , nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
