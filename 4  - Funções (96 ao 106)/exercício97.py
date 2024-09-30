def escreva(mensagem):
    linha = len(mensagem)+4
    print('-'*linha)
    print(f'  {mensagem}')
    print('-'*linha)

mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)
