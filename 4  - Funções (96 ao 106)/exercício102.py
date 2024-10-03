def fatorial(numero=0, show=False):
    fatorial = 1
    conta = ''
    for contador in range(1, numero+1):
        fatorial = fatorial * contador
        if show == True:
            if contador < numero:
                conta = conta + str(f'{contador} X ')
            else:
                conta = conta + str(f'{contador} = {fatorial}')
    if show == True:
        return print(conta)
    else:
        return print(fatorial)

fatorial(True)
