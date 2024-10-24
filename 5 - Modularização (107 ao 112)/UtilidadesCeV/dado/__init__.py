def leiaDinheiro(texto):
    numero = str(input(f'{texto}'))
    numero = numero.replace(',', '.')
    while numero.isalpha() == True:
        print('Invalido, digite novamente...')
        numero = str(input(f'{texto}'))
    numero = numero.replace(',', '.')
    return float(numero)
    