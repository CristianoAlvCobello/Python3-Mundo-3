def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')  
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero
def leiaReal(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return numero
        
inteiro = leiaInt('Digite um Inteiro: ')
real = leiaReal('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
