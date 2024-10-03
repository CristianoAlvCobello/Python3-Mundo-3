def leiaInt(texto):
    global leitura
    leitura = ''
    while leitura.isnumeric() != True:
        leitura = str(input(f'{texto}'))  
        if leitura.isnumeric() == False:
            print(f'\033[31mERRO! Digite um número inteiro válido\033[m')

leiaInt('Digite um número: ')
print(f'Você digitou o número {leitura}')
