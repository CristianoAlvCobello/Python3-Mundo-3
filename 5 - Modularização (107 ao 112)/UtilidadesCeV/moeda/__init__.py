def metade(valor=0, formatar=False):
    valor = valor/2
    if formatar == True:
        valor = str(valor)
        valor = valor.replace('.', ',')
    return valor

def dobro(valor=0, formatar=False):
    valor = valor*2
    if formatar == True:
        valor = str(valor)
        valor = valor.replace('.', ',')
    return valor

def aumentar(valor=0, porcentagem=0, formatar=False):
    valor = valor+(valor*porcentagem/100)
    if formatar == True:
        valor = str(valor)
        valor = valor.replace('.', ',')
    return valor

def diminuir(valor=0, porcentagem=0, formatar=False):
    valor = valor-(valor*porcentagem/100)
    if formatar == True:
        valor = str(valor)
        valor = valor.replace('.', ',')
    return valor

def moeda(valor):
    strvalor = str(valor)
    return strvalor.replace('.', ',')

def resumo(valor=0, aumento=0, redução=0):
    print(f'\nValor analisado: {valor}')
    print(f'Dobro do valor: {dobro(valor)}')
    print(f'Metade do valor: {metade(valor)}')
    print(f'{aumento}% de aumento: {aumentar(valor, aumento)}')
    print(f'{redução}% de aumento: {aumentar(valor, redução)}')
