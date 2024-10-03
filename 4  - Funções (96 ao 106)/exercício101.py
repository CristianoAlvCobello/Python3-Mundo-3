from datetime import date

def voto(nascimento):
    idade = date.today().year - nascimento
    print(f'Com {idade} anos:', end=' ')
    if idade <= 17:
        return print('VOTO NEGADO')
    elif idade >= 65:
        return print('VOTO OPCIONAL')
    else:
        return print('VOTO OBRIGATÓRIO')

nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)
